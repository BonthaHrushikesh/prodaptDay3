import json

from openai import skills

from openai import skills

user = {
    "id": 1,
    "name": "John Doe",
    "active": True,
    skills: ["Python", "JavaScript", "SQL"]

}

json_string = json.dumps(user, indent=4)
print(json_string)

json_dict = json.loads(json_string)
print(json_dict["name"])