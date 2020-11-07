glossary = {
    'variable': 'assing value',
    'list': 'collection of data',
    'condition': 'if statement is boolean expression',
    'dictionary': 'collection of data with key value pair',
    'tuple': 'collection of data like list but immutable',
    'loop': 'do repeated work',
    'comprehension': 'reduce code'
    }

# print(f"Varibale: {glossary['variable']}\n")
# print(f"List: {glossary['list']}\n")
# print(f"Condition: {glossary['condition']}\n")
# print(f"Dictionary: {glossary['dictionary']}\n")
# print(f"tuple: {glossary['tuple']}")

for key, value in glossary.items():
    print(f'{key}: {value}')