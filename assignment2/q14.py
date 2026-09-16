from typing import Union


def describe(x: Union[int, str]) -> str:
    if isinstance(x, int):
        return "number: {}".format(x + 1)

    return "text: {}".format(x.upper())


print(describe(10))
print(describe("hello"))