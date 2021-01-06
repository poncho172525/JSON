

import json


with open ('JSON.json', 'r') as file:
    JSON = json.load(file)



k = JSON['user']['name']

JSON['user']['name'] == 'Tech Lead'



print(k)


with open ('JSON.json', 'w') as file:
    json.dump(JSON,file)