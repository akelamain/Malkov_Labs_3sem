from typing import Iterable, Any
from gen_random import gen_random

class Unique(object):
    def __init__(self, data: Iterable[Any], case_sensitive: bool=True):
        self.sequence = iter(data)
        self.used_elements = dict()
        self.case_sensitive = case_sensitive

    def __next__(self) -> Any:
        while True:
            element = next(self.sequence)

            if isinstance(element, str) and not self.case_sensitive:
                key = element.lower()
            else:
                key = element

            if key not in self.used_elements:
                self.used_elements[key] = True
                return element

    def __iter__(self):
        return self
    
def main():
    print('---')

    for item in Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]):
        print(item)

    print('---')

    for item in Unique(gen_random(10, 1, 3)):
        print(item)

    data = ['Apple', 'Banana', 'apple', 'Orange', 'banana', 'Grape']

    print('---')

    for item in Unique(data, case_sensitive=False):
        print(item)

    print('---')

    for item in Unique(data, case_sensitive=True):
        print(item)
    
    return 0

if __name__ == "__main__":
    main()