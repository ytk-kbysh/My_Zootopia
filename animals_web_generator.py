import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
  
def load_html(file_path):
  """ Loads an html file """
  with open(file_path, "r") as data:
    return data.read()
  
def rewrite_html(file_path, new_data):
  """ Loads an html file """
  with open(file_path, "w") as data:
    return data.write(new_data)
  
def serialize_animal(item):
  output = ''
  output += '            <li class="cards__item">\n'
  output += f'                <div class="card__title"> {item['name']} </div>\n'
  output += f'                <p class="card__text">\n'
  output += f"                    <ul>"
  output += f"                        <li><strong>Diet:</strong> {item['characteristics']['diet']} </li>\n"
  output += f"                        <li><strong>Location:</strong> {item['locations'][0]}</li>\n"
  try:
      output += f"                        <li><strong>Type:</strong> {item['characteristics']['type']}</li>\n"
  except:
      pass
  output += f"                    </ul>"
  output += f"               </p>\n"
  output += "            </li>\n"

  return output
   
animals_data = load_data('animals_data.json')

html_data = load_html('animals_template.html')

output = ''  # define an empty string

for animalobj in animals_data:
    # append information to each string
    output += serialize_animal(animalobj)

re_html = html_data.replace("__REPLACE_ANIMALS_INFO__", output)

rewrite_html('animals_template.html', re_html)