""".
This code print random Pokémon, or Pokémon with flags
"""
import argparse
import random

from constants import POKEMONS


def create_parser():
    parser = argparse.ArgumentParser(description="Filter Pokémon")
    parser.add_argument('-a', '--arms', action='store_true', help='Show Pokémon with arms')
    parser.add_argument('-t', '--tail', action='store_true', help='Show Pokémon with tail')
    parser.add_argument('-f', '--fly', action='store_true', help='Show Pokémon that can fly')
    return parser


def print_pokemon(args, list_of_pokemons):
    if not args.arms and not args.tail and not args.fly:
        filtered_list = list_of_pokemons
    else:
        filtered_list = [pokemon for pokemon in POKEMONS if
                         (not args.arms or args.arms == pokemon['arms']) and
                         (not args.tail or args.tail == pokemon['tail']) and
                         (not args.fly or args.fly == pokemon['fly'])]
    print(random.choice(filtered_list)['name'])


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    print_pokemon(args, POKEMONS)
