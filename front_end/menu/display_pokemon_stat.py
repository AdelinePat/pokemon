import pygame
from back_end.controller import create_player
# from select_pokemons import SelectPokemons

class PokemonStat():
    def __init__(self, player_name, pokemon_list, pokemon, screen):
        self.player_name = player_name
        self.pokemon_list = pokemon_list
        self.pokemon = pokemon
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
       
        self.selected_index = 0
        self.running = True

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.screen.get_display().blit(surface, rect)

    def display(self):
        while self.running:
            self.screen.update()
            self.screen.get_display().fill((0, 0, 0))

            # text = f"{self.pokemon.name}\
            #     \n"original_name : {self.get_original_name()}\
            # pet_name : {self.pet_name}
            # hp : {self.get_hp()}
            # xp : {self.get_xp()}
            # strength : {self.get_strength()}
            # defense : {self.get_defense()}
            # type : {self.type}
            # level : {self.get_level()}
            # speed :{ self.get_speed()}
            # stage : {self.get_stage()}
            # ev : self.get_effort_value().get_ev_dict()
            # state : self.get_state()"

            text= f"{self.pokemon}"

            y_position = self.screen.heigth // 2

            self.draw_text(self.pokemon.name, self.screen.width//2, y_position -175, (255, 255, 0))
            self.draw_text(f"Level : {str(self.pokemon.get_level())}", self.screen.width//2, y_position - 125, (255, 255, 0))
            self.draw_text(f"Type : {str(", ".join(self.pokemon.type))}", self.screen.width//2, y_position -75, (255, 255, 0))
            self.draw_text(f"HP : {str(self.pokemon.get_hp())}", self.screen.width//2, y_position -25, (255, 255, 0))
            self.draw_text(f"Strength : {str(self.pokemon.get_strength())}", self.screen.width//2, y_position + 25, (255, 255, 0))
            self.draw_text(f"Defense : {str(self.pokemon.get_defense())}", self.screen.width//2, y_position + 75, (255, 255, 0))
            self.draw_text(f"Speed : {str(self.pokemon.get_speed())}", self.screen.width//2, y_position + 125, (255, 255, 0))
            self.draw_text(f"XP : {str(self.pokemon.get_xp())}", self.screen.width//2, y_position + 175, (255, 255, 0))
            

            # for i, option in enumerate(self.options):
            #     color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
            #     self.draw_text(option, 600, 300 + i * 60, color)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)

                    elif event.key == pygame.K_RETURN:
                                # PokemonStat(self.pokemons[index], self.screen)
                            # create_player(self.player_name, self.pokemon)
                            create_player(self.player_name, self.pokemon)
                            return self.pokemon
                    elif event.key == pygame.K_ESCAPE:
                        from .select_pokemons import SelectPokemons
                        return SelectPokemons(self.player_name, self.screen, self.pokemon_list).display()