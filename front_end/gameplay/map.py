import pygame
import pytmx
import pyscroll
from front_end.screen import Screen
from .switch import Switch
from front_end.gameplay.in_fight import InFight
from front_end.sounds import Sounds
# from front_end.menu.pause_menu import PauseMenu

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
        self.current_map: Switch = Switch("switch", "map_0", pygame.Rect(0, 0, 0, 0), 0)
        self.switch_map(self.current_map)
        self.map_world = "map_0"



       
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
            print(obj.name)
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

                # Gestion du changement de musique
        # Arrêter la musique actuelle
        sounds.stop_map_music()

        # Déterminer la musique à jouer en fonction du nom de la map
        if switch.name.startswith("house_"):
            sounds.play_maison_music()
        elif switch.name.startswith("pokeshop"):
            sounds.play_pokeshop_music()
        elif  switch.name.startswith("pokecenter"):
            sounds.play_pokecenter_music()
        elif  switch.name.startswith("labo_"):
            sounds.play_labo_music()
        elif switch.name.startswith("inter_"):
            sounds.play_labo_music()
        else:
            sounds.play_map_music()  # Par défaut, jouer la musique de la map


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
                # Si le joueur quitte une maison (ou entre dans 

               
                # if self.player.change_map == self.map_world:  # 

                    # Effectue le changement de carte
                    self.switch_map(self.player.change_map)
                

                    self.player.change_map = None  # Réinitialise le changement de carte






            this_battle_zone = (0,0,0,0)
            # Check for collision with battle zones
            for battle_zone in self.battlepokemon:
                if self.player.rect.colliderect(battle_zone) and not self.in_battle:
                    sounds.stop_map_music()  # Stop map music
                    sounds.play_combat_music()  # Play combat music
                    self.in_battle = True  # Set the flag for battle
                    self.player.is_fleeing = self.start_battle()  # Start the Pokémon battle
                    this_battle_zone = battle_zone
                    if not self.player.is_fleeing:
                        self.player.keyListener.keys = []
                   
                    

                if self.player.rect.colliderect(battle_zone) and self.in_battle:
                    this_battle_zone = battle_zone
                # break
            
            if not self.player.rect.colliderect(this_battle_zone) and self.in_battle:
                self.in_battle = False
                sounds.play_map_music()

           

        # Update all sprites and center the map
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())

    def start_battle(self):
        # # Start a battle when the player enters a battle zone
        # print("Starting Pokémon battle! dans start_battle")
        battle_screen = InFight(self.screen, self.player, self.player.active_pokemon).display()
        self.player.keyListener.clear()#clear the keylistener
        self.player.flee_steps = 0
        return battle_screen
 
    def pose_player(self, switch: Switch):
        # Set player's spawn position based on map
        position = self.tmx_data.get_object_by_name("spawn " + self.current_map.name + " " + str(switch.port))
        self.player.position = pygame.math.Vector2(position.x, position.y)
