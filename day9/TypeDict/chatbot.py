from typing import Sequence, TypedDict, Union

InputData =Union[str,bytes]

def chatbots(inputs:Sequence[InputData]) -> None:
    for item in inputs:
        if isinstance(item, str):
            print(f"User Text: {item}")
        else:
            print(f"User Bytes: {item}")

        