""".
This code print random Pokémon, or Pokémon with flags
"""
import argparse
from random import choice

from constants import POKEMONS

parser = argparse.ArgumentParser(description='Choice pokemon')
parser.add_argument('-f', '--flying', action='store_true', help='Pokemons that have wings or can fly')
parser.add_argument('-a', '--arm', action='store_true', help='Pokemons that have arm/arms')
parser.add_argument('-t', '--tailed', action='store_true', help='Pokemons that have tails')
args = parser.parse_args()


def show_pokemon():
    """
    This function processes flags and give Pokémon.
    """
    selected_pokemon = []

    if args.flying:
        selected_pokemon.append(set(POKEMONS['fly']))
    if args.arm:
        selected_pokemon.append(set(POKEMONS['have_hands']))
    if args.tailed:
        selected_pokemon.append(set(POKEMONS['tails']))
    if not any([args.flying, args.arm, args.tailed]):
        all_pokemon = set(POKEMONS['fly'] + POKEMONS['have_hands'] + POKEMONS['tails'])
        selected_pokemon.append(all_pokemon)

    if selected_pokemon:
        common_pokemon = list(set.intersection(*selected_pokemon))
        if common_pokemon:
            print('Selected Pokemon:')
            print(choice(common_pokemon))
        else:
            print('Dont found pokemon.')
    else:
        print('Other error.')


if __name__ == '__main__':
    show_pokemon()
