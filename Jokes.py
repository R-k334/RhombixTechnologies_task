import requests

def joke():

    url = "https://official-joke-api.appspot.com/random_joke"  
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        json_data = response.json()  
        setup = json_data["setup"]
        punchline = json_data["punchline"]
        
        return [setup, punchline]  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")  
        return ["Sorry, I couldn't fetch a joke right now.", ""]  