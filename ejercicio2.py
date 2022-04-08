from random import random
from ejercicio1 import Pokemon


class PokemonTierra(Pokemon):
    def __init__(self,ID,nombre,arma,ataque,salud,defensa):
        super().__init__(ID,nombre,arma,ataque,salud,defensa)
        if isinstance(defensa,int):
            if defensa >= 11 and defensa <= 20:
                self._defensa = defensa
            else:
                raise ValueError
        else:
            raise TypeError
class PokemonAgua(Pokemon):
    def __init__(self,ID,nombre,arma,ataque,salud,defensa):
        super().__init__(ID,nombre,arma,ataque,salud,defensa)
        if isinstance(ataque,int):
            if ataque >= 11 and ataque <= 20:
                self._ataque = ataque
            else:
                raise ValueError
        else:
            raise TypeError
class PokemonAire(Pokemon):
    def __init__(self,ID,nombre,arma,ataque,salud,defensa):
        super().__init__(ID,nombre,arma,ataque,salud,defensa)
        
    def fight_defense(self,daño):
        if not isinstance(daño,int):
            raise TypeError
        print(self._nombre + "recibió un ataque de" + str(daño) + "puntos")
        posibilidadnoafecte = random.randrange(0,2)
        if daño > self._defensa:
            self._salud = (self._salud-self.daño)
            pokemonatacado = True
        else:
            print("No ha sido dañado")
            pokemonatacado = False
        return pokemonatacado
class PokemonElectricidad(Pokemon):
    def __init__(self,ID,nombre,arma,ataque,salud,defensa):
        super().__init__(ID,nombre,arma,ataque,salud,defensa)
    def fight_attack(self,pokemon_to_attack):
        daño = self._ataque
        print(self._nombre + "atacó a" + pokemon_to_attack.get_nombre() + "con" + str(daño) + "puntos")
        posibilidadafecte = random.randrange(0,2)
        pokemonatacado = pokemon_to_attack.fight_defense(daño)
        return pokemonatacado