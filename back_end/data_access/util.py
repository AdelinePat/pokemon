
from back_end.models.pokemon import Pokemon
from ..models.bag import Bag

def instanciate_pokemon(pokemon):
    my_pokemon = Pokemon(pokemon['name'], pokemon['original_name'], pokemon['hp'],\
                        pokemon['strength'], pokemon['defense'], pokemon['type'],\
                        pokemon['level'], pokemon['speed'], pokemon['stage'])
    
    my_pokemon.set_xp(pokemon['xp'])
    my_pokemon.set_state(pokemon['state'])
    my_pokemon.get_effort_value().set_ev_hp(pokemon['ev']['hp'])
    my_pokemon.get_effort_value().set_ev_strength(pokemon['ev']['strength'])
    my_pokemon.get_effort_value().set_ev_defense(pokemon['ev']['defense'])
    my_pokemon.get_effort_value().set_ev_speed(pokemon['ev']['speed'])
    my_pokemon.get_effort_value().set_ev_xp(pokemon['ev']['xp'])

    my_pokemon.set_pet_name(pokemon['pet_name'])

    return my_pokemon

def instanciate_bag(player):
    # player is the dictionary of player name in player_pokedex.json
    player_bag = Bag()
    player_bag.set_potion(player["bag"]["potion"])
    player_bag.set_pokeball(player["bag"]["pokeball"])

    return player_bag