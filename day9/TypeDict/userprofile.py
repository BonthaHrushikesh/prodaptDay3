from typing import List, Optional, TypedDict

class userprofile(TypedDict):
    id:int
    name:str
    email:str
    bio: Optional[str]

def format_user_profile(users:List[userprofile]) -> List[str]:
    return [f"{u['name']} ({u['email']})" for u in users]

users=[
    {"id": 1, "name": "Alice", "email": "alice@example.com", "bio": "Software Engineer"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "bio": "Data Scientist"}
]

print(format_user_profile(users))   