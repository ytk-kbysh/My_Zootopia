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

animals_data = load_data('animals_data.json')
html_data = load_html('animals_template.html')

# i = 1
# for line in html_data:
#     print(f"line {i} : {line}")
#     i += 1

# for item in animals_data:
#     print(f"Name: {item['name']}")
#     print(f"Diet: {item['characteristics']['diet']}")
#     print(f"Location: {item['locations'][0]}")
#     try:
#         print(f"Type: {item['characteristics']['type']}")
#     except:
#         pass

output = ''  # define an empty string
for item in animals_data:
    # append information to each string
    output += '            <li class="cards__item">\n'
    output += f"            Name: {item['name']}<br/>\n"
    output += f"            Diet: {item['characteristics']['diet']}<br/>\n"
    output += f"            Location: {item['locations'][0]}<br/>\n"
    try:
        output += f"            Type: {item['characteristics']['type']}<br/>\n"
    except:
        continue
    output += "            </li>\n"

re_html = html_data.replace("__REPLACE_ANIMALS_INFO__", output)

rewrite_html('animals_template.html', re_html)