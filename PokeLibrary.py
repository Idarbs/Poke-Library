import requests, time

# This Project Uses The PokeAPI. It Can Be Used To Search For Pokemon Information.

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}" # The user input is added to the website path
    response = requests.get(url) # Program checks with the API to search that path
    if response.status_code == 200: # HTTP Code 200 = Success
        time.sleep(1)
        print("Pokemon Found!")
        time.sleep(1)
        poke_data = response.json() # This captures the ENTIRE dictionary and stores it into a variable
        return poke_data
    else: # Captures any other code besides 200, usually a 404 meaning not found
        print(f"Pokemon Not Found, Try A Different Pokemon Name. Code: {response.status_code}.")

while True: # Program will always run until user inputs X
    print("What Pokemon Would You Like To Search For? Enter a Name Or Type 'X' To Quit.")
    pokemon_name = input() # User inputs a pokemon name
    if pokemon_name.isalpha() and not pokemon_name.upper() == 'X': # Validates user input
        poke_info = get_pokemon_info(pokemon_name)
        if poke_info: # Will always be true
            print(f"Name: {poke_info["name"]}".title()) # Displays its name
            print(f"Height: {poke_info["height"]} feet") # Displays height in feet
            print(f"Weight: {poke_info["weight"]} pounds") # Displays weight in pounds
            print(f"Pokedex ID: {poke_info["id"]}") # Displays the Pokemon's Pokedex ID
            
            # Parses through the types object and grabs the key paired values
            for type_info in poke_info['types']:
                type_name = type_info['type']['name']
                print(f"Typing: {type_name}".title()) # Displays the Pokemon's typing(s)
            
            # Parses through the abilities object and grabs the key paired values
            for ability_info in poke_info['abilities']:
                ability_name = ability_info['ability']['name']
                print(f"Ability Name: {ability_name}".title()) # Displays its abilities
            
            # Parses through the stats object, pulls out the integers, stat name, etc
            for stat_info in poke_info['stats']:
                stat_type = stat_info['stat']['name']
                base_stat = stat_info['base_stat']
                print(f"Stat: {stat_type.title()} - Base Value: {base_stat}")
            
            # Parses through the game_indices object and grabs the key paired values
            for game_info in poke_info['game_indices']:
                game_name = game_info['version']['name']
                print(f"Game Title: Pokemon:{game_name}".title()) # This displays every game the Pokemon is in
    
    elif pokemon_name.upper() == 'X': # Quits the program
        break
    
    else: # User must enter a valid input
        print("No Numbers Or Special Characters Allowed!")
        pokemon_name = input()