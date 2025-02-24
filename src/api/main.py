from fastapi import FastAPI
from fastapi import HTTPException
import  httpx

app = FastAPI()


async def fetch_pokemon_data(url:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Pokémon not found")
        return response.json()

@app.get("/api/pokemon_ability/{pokemon_name}/")
async def get_pokemon_ability(pokemon_name: str):
    pokemon_ability_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    
    data =  await fetch_pokemon_data(pokemon_ability_url)
    abilities = [ability['ability']['name'] for ability in data.get('abilities', [])]
    
    return {"abilities": abilities}
        
@app.get("/api/pokemon_color/{pokemon_name}")
async def get_pokemon_color(pokemon_name:str):
    pokemon_color_url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/'
    
    data = await fetch_pokemon_data(pokemon_color_url)
        
    color = data.get("color", {}).get("name", "unknown")
    
    return {"color": color}
        
        
@app.get("/api/pokemon_details/{pokemon_name}/")
async def get_pokemon_details(pokemon_name:str):
    species_data = await fetch_pokemon_data(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/')
    pokemon_data = await fetch_pokemon_data(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
    color = species_data.get("color", {}).get("name", "unknown")
    gender_rate = species_data.get("gender_rate", -1)  
    abilities = [ability['ability']['name'] for ability in pokemon_data.get('abilities', [])]
    description = next(
        (entry['flavor_text'] for entry in species_data.get("flavor_text_entries", []) if entry["language"]["name"] == "en"),
        "No description available"
    )
    return {
        "pokemon_name": pokemon_name,
        "color": color,
        "gender_rate": gender_rate,
        "abilities": abilities,
        "description": description
    }

                
                 
