from fastapi import FastAPI
from fastapi import HTTPException
import  httpx

app = FastAPI()


pokemon_ability:str = ''
pokemon_color:str = ''


# the element actually being passed is the pokemons name in the request from the client for (pokemon ability and pokemon color)
@app.get("/api/pokemon_details")
def read_root():
    return {'Hello': 'hi mum'}

@app.get("/api/pokemon_ability/{pokemon_ability}/")
async def get_pokemon_ability(pokemon_ability: str):
    pokemon_ability_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_ability}/'
    async with httpx.AsyncClient() as client:
        response = await client.get(pokemon_ability_url)
        if response.status_code != 200:
             raise HTTPException(status_code=404, detail="pokemon not found")
        data =  response.json()
        
        for ability in data.get('abilities',[]):
            ability_names = ability['ability']['name']
            pokemon_ability = ability_names
            return {
                "ability":pokemon_ability
            }
        
@app.get("/api/pokemon_color/{pokemon_color}")

async def get_pokemon_color(pokemon_color:str):
    pokemon_color_url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_color}/'
    async with httpx.AsyncClient() as client:
        response  = await client.get(pokemon_color_url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="pokemon not found")
        
        
        data = response.json()
        iterate:int = 0
        data_values:list= []
        color_dict = ''
        color:str = ''
        while iterate < len(data):
            
            for x in data:
                data_values.append(data[x])
            iterate = iterate + 1
        
        second_iterate:int = 0
    
        
        while second_iterate < len(data_values):
            second_iterate = second_iterate + 1
            for el in data_values:
                if isinstance(el,dict):
                    if 'name' in el:
                        color_dict = el
                        break
        for el in color_dict.values():
            color =  el
            return {
                "color":color
            }
            
        
                
                 
