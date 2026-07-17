from typing import Sequence

def process_management(message: Sequence[str]) -> None:
    print("message received")
    for m in message:
        print(m)


text_tuple = (
    "checking the input",
    "Tuple input",
    "working or not"
)

process_management(text_tuple)
