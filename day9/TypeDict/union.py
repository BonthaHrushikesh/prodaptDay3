from typing import TypedDict, Union

def process_input(data:Union[str, bytes]) -> None:
    if isinstance(data, str):
        print(f"Processing Text data: {data}")
    elif isinstance(data, bytes):
        print(f"Processing bytes data: data")
    
print(process_input("Hello, World!"))

print(process_input(b'\x89PNG\r\n'))
