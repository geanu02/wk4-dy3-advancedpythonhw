from LinkedList import LinkedList
from Pokemon import Pokemon

charmander = Pokemon('charmander')
evo_data = charmander.get_evolution_chain()

print(evo_data['evolves_to'][0]['species']['name'])