
import back_end.data_access.player_pokedex_service as player_pokedex_service
import back_end.data_access.pokemon_pokedex_service as pokemon_pokedex_service
import back_end.data_access.wild_pokemons as wild_pokemons
import back_end.data_access.bag_pokedex_service as bag_pokedex_service

# Player pokedex service
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

def does_player_exist(player):
    is_player = player_pokedex_service.does_player_exist(player)
    return is_player

# Pokemon pokedex service
def get_all_pokemons_from_pokedex(player_name):
    pokemon_list = pokemon_pokedex_service.get_all_pokemons_from_pokedex(player_name)
    return pokemon_list

def get_first_pokemon(player_name):
    pokemon = pokemon_pokedex_service.get_first_pokemon(player_name)
    return pokemon

def save_pokemon_to_pokedex(player, pokemon):
    pokemon_pokedex_service.save_pokemon_to_pokedex(player, pokemon)

# Wild pokemon
def get_random_wild_pokemon():
    return wild_pokemons.get_random_wild_pokemon()

def save_wild_pokemon(my_pokemon):
    wild_pokemons.save_wild_pokemon(my_pokemon)

# Bag
def get_bag_from_pokedex(player):
    bag = bag_pokedex_service.get_bag_from_pokedex(player)
    return bag

def save_bag_to_pokedex(player, bag):
    bag_pokedex_service.save_bag_to_pokedex(player, bag)