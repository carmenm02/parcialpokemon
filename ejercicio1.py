from enum import Enum

class Pokemon():
    lista=[]
    def __str__(self):
        return self.nombre

def __init__(self, ID,nombre,arma,salud,ataque,defensa):
    if ID not in Pokemon.lista:
        self.ID = ID
        Pokemon.lista.append(self.ID)
    else:
        raise TypeError
    if isinstance(nombre,str):
        self._nombre = nombre
    else:
        raise TypeError
    if isinstance(arma,str):
        self._arma = arma
    else:
        raise TypeError
    if isinstance(salud,int):
        if salud >= 1 and salud <= 100:
            self._salud = salud
        else:
            raise ValueError
    else:
        raise TypeError
    if isinstance(ataque,int):
        if ataque>=1 and ataque <= 10:
            self._ataque = ataque
        else:
            raise ValueError
    else:
        raise TypeError
    if isinstance (defensa,int):
        if defensa>=1 and defensa<=10:
            self._defensa=defensa
        else:
            raise ValueError
    else:
        raise TypeError

def get_ID(self):
    return self._pokemon_ID
def get_nombre(self):
    return self._pokemon_nombre
def get_arma(self):
    return self._pokemon_arma
def get_salud(self):
    return self._pokemon_salud
def get_ataque(self):
    return self._pokemon_ataque
def get_defensa(self):
    return self._pokemon_defensa

def set_nombre(self,nombredelpokemon):
    if isinstance(nombredelpokemon,str):
        self._nombre = nombredelpokemon
    else:
        raise TypeError
def set_arma(self,armadelpokemon):
    if isinstance(armadelpokemon,str):
        self._arma = armadelpokemon
    else:
        raise TypeError
def set_ataque(self,ataquedelpokemon):
    if isinstance(ataquedelpokemon,int):
        if ataquedelpokemon >=1 and ataquedelpokemon<=100:
            self._ataque = ataquedelpokemon
        else:
            raise ValueError
    else:
        raise TypeError
def set_defensa(self,defensadelpokemon):
    if isinstance(defensadelpokemon,int):
        if defensadelpokemon >=1 and defensadelpokemon <= 10:
            self._defensa = defensadelpokemon
        else:
            raise ValueError
    else: raise TypeError

def is_alive(self):
    return not bool(self._salud == 0)

def fight_attack(self,pokemon_to_attack):
    daño = self._ataque
    print(self._nombre + "atacó a" + pokemon_to_attack.get_nombre() + "con" + str(daño) + "puntos")
    pokemonatacado = pokemon_to_attack.fight_defense(daño)
    return pokemonatacado
def fight_defense(self,daño):
    if not isinstance(daño,int):
        raise TypeError
    print(self._nombre + "recibió un ataque de" + str(daño) + "puntos")
    if daño > self._defensa:
        self._salud = (self._salud-self.daño)
        pokemonatacado = True
    else:
        print("No ha sido dañado")
        pokemonatacado = False
    return pokemonatacado

