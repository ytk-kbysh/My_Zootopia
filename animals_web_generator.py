import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
  

  animals_data = load_data('animals_data.json')

for item in load_data('animals_data.json'):
    print(f"Name: {item['name']}")
    print(f"Diet: {item['characteristics']['diet']}")
    print(f"Location: {item['locations'][0]}")
    try:
        print(f"Type: {item['characteristics']['type']}")
    except:
        pass
