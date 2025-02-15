
import back_end.player_pokedex_service as player_pokedex_service

def get_player_names():
    player_names = list(player_pokedex_service.get_player_names())
    return player_names

def get_player_pokemons(player):
    player_pokemons = list(player_pokedex_service.get_player_pokemons(player))
    return player_pokemons

def create_player(player, pokemon):
    player_pokedex_service.create_player(player, pokemon)

def get_starter_pokemons():
    pokemon_list = []
    for index in range(3):
        pokemon = player_pokedex_service.get_starter_pokemon()
        pokemon_list.append(pokemon)
    return pokemon_list