import requests

# Write a function which takes in a page number and prints all pokemon on that page.
# 20 per page.
#
# get_page(5) => from 100 to 120

def get_page_offset(page_no, offset=20):
    return page_no * offset

def get_pokemon_page(get_limit, get_offset):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={get_limit}&offset={get_offset}"
    response = requests.get(url)
    return response.json()

#add function to print a specified pokemon, and info on that
#id, name, type
def get_specified_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    print(response.json()["abilities"])

# use print_results to print page 1 in a numbered list
def print_numbered_list(list_of_items):
    for idx, item in enumerate(list_of_items):
        print(f"{idx} {item['name']}")

def print_results(page_no, limit=20):
    get_offset = get_page_offset(page_no)
    list_to_print = get_pokemon_page(limit, get_offset)["results"]
    print_numbered_list(list_to_print)

#print_results(2)
get_specified_pokemon(3)

# add a input
 #print("What pokemon do you want to see")
 #specified_pokemon = input()

# use input to print pokemon with the numberinput