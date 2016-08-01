import json

# open file 'config.json'
file = open('config.json')

# load file 'config.json' to json object
config = json.load(file)

# read object 'zhihu' in json object
print(config['zhihu'])

