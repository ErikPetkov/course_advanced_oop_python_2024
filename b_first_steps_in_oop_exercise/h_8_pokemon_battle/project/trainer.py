from project import Pokemon
class Trainer:
    def __init__(self,name:str):
        self.name = name
        self.pokemons = list()

    def add_pokemon(self,pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self,pokemon_name: string) -> str:
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        res = ''
        res+= f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for p in self.pokemons:
            res+= f"- {self.pokemons}"
