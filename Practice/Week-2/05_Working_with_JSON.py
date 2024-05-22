print("\n###-PARSING JSON-###\n")

import json


jData = '{ "name": "virendra", "year": 3 }'


pData = json.loads(jData)

print("Type of jData: ", type(jData))
print("Type of pData: ", type(pData))

print(pData["name"])



print("\n###-PYTHON TO JSON-###\n")

pObj = {
    "name": "virendra",
    "college": "JIET"
}

jObj = json.dumps(pObj)

print("Type of pObj: ", type(pObj))
print("Type of jObj: ", type(jObj))

