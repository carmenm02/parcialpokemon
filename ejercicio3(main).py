import csv
import copy

from ejercicio1 import Pokemon

def get_data_from_user(name_file):
    set_of_pokemons = []

    if not isinstance(name_file,str):
        raise TypeError()
    
    name_files = name_file

    try:
        with open(name_files,newline=" ") as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)

        for temp_pokemon_csv in data_from_file:
            coach_pokemon = Pokemon(int(temp_pokemon_csv[0]),temp_pokemon_csv[1],temp_pokemon_csv[3],temp_pokemon_csv[4],temp_pokemon_csv[5])
            set_of_pokemons.append(coach_pokemon)
    except SyntaxError:
        print("Intentalo de nuevo")
    return set_of_pokemons

def get_pokemon_in_a_list_of_pokemons(coach_to_ask,list_of_pokemons):
    if isinstance(list_of_pokemons,list):
        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError()
        print(str(coach_to_ask) + "introduce el ID del pokemon: " + "\n")

        while True:
            print("Lista de Pokemons: " + "\n")

            for i in list_of_pokemons:
                print(i)
            
            string_introducida = input("")
            try:
                int_introduced = int(string_introducida)
            except ValueError:
                print("Porfavor introduce un ID de la lista")
            for temp_pokemon in list_of_pokemons:
                if int_introduced == temp_pokemon.get_id():
                    return temp_pokemon
            print("Porfavor introduce un numero de la lista")
    else:
        raise TypeError()

def coach_is_undefeated(list_of_pokemons):
    if isinstance(list_of_pokemons,list):
        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon,Pokemon):
                raise TypeError()
    
    defeated = True

    for temp_pokemon in list_of_pokemons:
        if temp_pokemon.is_alive():
            defeated = False
    return not defeated

def main():

    print("Comienza el juego")
    
    print("Datos del jugador 1: \n")
    game_user_1 = get_data_from_user("coach_1_pokemons.csv")

    print("Datos del jugador 2: \n")
    game_user_2 = get_data_from_user("coach_2_pokemons.csv")

    temp_list_pokemons_from_coach_1 = game_user_1
    list_pokemons_alive_coach_1 = copy.copy(temp_list_pokemons_from_coach_1)
    temp_list_pokemons_from_coach_2 = game_user_2
    list_pokemons_alive_coach_2 = copy.copy(temp_list_pokemons_from_coach_2)

    print("Elige tu primer pokemon entrenador 1")
    temp_list_pokemons_from_coach_1 = get_pokemon_in_a_list_of_pokemons("Introduce el ID del pokemon:", list_pokemons_alive_coach_1)
    print("Elige tu primer pokemon entrenador 2")
    temp_list_pokemons_from_coach_2 = get_pokemon_in_a_list_of_pokemons("Introduce el ID del pokemon:",list_pokemons_alive_coach_2)

    while(coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        if not temp_list_pokemons_from_coach_1.is_alive():
            print("Entrenador 1, tu pokemon " + str(temp_pokemon_coach_1)+"ha sido derrotado, elige otro")
            list_pokemons_alive_coach_1.remove(temp_pokemon_coach_1)
            temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons

        if not temp_list_pokemons_from_coach_2.is_alive():
            print("Entrenador 2, tu pokemon " + str(temp_pokemon_coach_2)+"ha sido derrotado, elige otro")
            list_pokemons_alive_coach_2.remove(temp_pokemon_coach_2)
            temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons
        
        print("Ataca el pokemon del entrenador 1")
        temp_pokemon_coach_1.fight_attack(temp_pokemon_coach_2)
        print("Ataca el pokemon del jugador 2")
        temp_pokemon_coach_2.fight_attack(temp_pokemon_coach_1)

    print("El juego ha terminado")

    if (coach_is_undefeated(temp_list_pokemons_from_coach_1) and not coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("Gana el jugador 1")
    elif(not coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("Gana el jugador 2")
    else:
        print("Ambos pierden")

    print("Entrenador 1:")
    for temp_pokemon in temp_list_pokemons_from_coach_1:
        print(temp_pokemon)
    print("Entrenador 2:")
    for temp_pokemon in temp_list_pokemons_from_coach_2:
        print(temp_pokemon)


if __name__ == "__main__":
    main()