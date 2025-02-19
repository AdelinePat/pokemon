import pygame
import pytmx
import pyscroll
# from .player import Player
from front_end.screen import Screen
from .switch import Switch
# from front_end.gameplay.battlescreen import BattleScreen
from front_end.in_fight.in_fight import InFight
# from Pokemon import PokemonBattle  # Import the PokemonBattle class
from front_end.sounds import Sounds
from front_end.menu.pause_menu import PauseMenu

sounds = Sounds()

class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.player = None
        self.switchs = None
        self.collisions = None
        self.battlepokemon = None
        self.in_battle = False  # Track if battle is in progress
        self.current_map: Switch = Switch("switch", "map0", pygame.Rect(0, 0, 0, 0), 0)
        self.switch_map(self.current_map)
       

    def switch_map(self, switch: Switch):
        self.tmx_data = pytmx.load_pygame(f"assets/map/{switch.name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

                # Adjust zoom level based on map type
        if switch.name.split("_")[0] == "map":
            self.map_layer.zoom = 3
        else:
            self.map_layer.zoom = 3.75

        self.switchs = []
        self.collisions = []
        self.battlepokemon = []
        
        # Loop through all objects to set up the map
        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            elif obj.name == "collisionpokemon":
                
                self.battlepokemon.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            # Add switches and other objects to the map
            elif obj.name and obj.name.startswith("switch"):
                type = obj.name.split(" ")[0]
                self.switchs.append(Switch(
                    type,
                    obj.name.split(" ")[1],
                    pygame.Rect(obj.x, obj.y, obj.width, obj.height),
                    int(obj.name.split(" ")[-1])
                ))

        # Set up player if initialized
        if self.player:
            self.pose_player(switch)
            self.player.align_hitbox()
            self.player.step = 16
            self.player.add_switchs(self.switchs)
            self.player.add_collisions(self.collisions)
            self.player.start_battle(self.battlepokemon)
            self.group.add(self.player)

        # Update the current map after switching
        self.current_map = switch

    def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()
        self.player.add_switchs(self.switchs)
        self.player.add_collisions(self.collisions)
        self.player.start_battle(self.battlepokemon)

    def update(self) -> None:
       
        if self.player:
            if self.player.change_map and self.player.step >= 8:
                self.switch_map(self.player.change_map)
                self.player.change_map = None

            this_battle_zone = (0,0,0,0)
            # Check for collision with battle zones
            for battle_zone in self.battlepokemon:
                if self.player.rect.colliderect(battle_zone) and not self.in_battle:
                    sounds.stop_background_music()  # Stop map music
                    sounds.play_combat_music()  # Play combat music
                    self.in_battle = True  # Set the flag for battle
                    self.player.is_fleeing = self.start_battle()  # Start the Pokémon battle
                    this_battle_zone = battle_zone
                    if not self.player.is_fleeing:
                        self.player.keyListener.keys = []
                    sounds.stop_background_music()
                    sounds.play_map_music()
                    # battle_screen = InFight(self.screen, self.player).display()
                    # battle_screen.run()
                    # is_fleeing = battle_screen.fleeing

                if self.player.rect.colliderect(battle_zone) and self.in_battle:
                    this_battle_zone = battle_zone
                # break
            
            if not self.player.rect.colliderect(this_battle_zone) and self.in_battle:
                self.in_battle = False

           

        # Update all sprites and center the map
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())

    def start_battle(self):
        # # Start a battle when the player enters a battle zone
        # print("Starting Pokémon battle!")
        # battle_screen = BattleScreen(self.screen, self.player)
        # battle_screen.run()
         # Start a battle when the player enters a battle zone
        print("Starting Pokémon battle! dans start_battle")
        battle_screen = InFight(self.screen, self.player, self.player.active_pokemon).display()
        self.player.flee_steps = 0
        return battle_screen
        
        # battle_screen.run()
        # InFight(self.screen, self.player).display().run()
        # battle_screen.run()
        # JOSEPH??
        # print("Starting Pokémon battle!")
        # battle_screen = PokemonBattle()  # Create instance of PokemonBattle
        # battle_screen.run()  # Run the battle

    def pose_player(self, switch: Switch):
        # Set player's spawn position based on map
        position = self.tmx_data.get_object_by_name("spawn " + self.current_map.name + " " + str(switch.port))
        self.player.position = pygame.math.Vector2(position.x, position.y)
