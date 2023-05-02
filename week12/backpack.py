from typing import Sequence
from string import ascii_lowercase




import random
class BackPack:

    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items: Sequence):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        # self._backpack.sort()

    def __len__(self):
        return len(self._backpack)

    def __getitem__(self, index):
        return self._backpack[index]

    # def sort(self):
    #     self._backpack.sort()

    # def count(self):
    #     return self._backpack.count()

    # def list(self):
    #     return self._backpack

    # def add(self, item):
    #     if item is not None:
    #         self._backpack.append(item)
    #         self.sort()

    # def in_backpack(self, item):
    #     """
    #     Complete this method using a binary search
    #     returns -1 or False if not found
    #     returns position if found
    #     :param item:
    #     :return: -1 | False | integer
    #     """
    #     return None

if __name__ == '__main__':
    shuffled_items = list(ascii_lowercase)
    random.shuffle(shuffled_items)
    backpack = BackPack(shuffled_items)
    print("Number of items:", len(backpack))
    print("Iterate over every item in the backpack:")
    for item in backpack:
        print(item)

    print(list(backpack))
    print(sorted(backpack))
    print("Is 'a' in backpack", 'a' in backpack)

##### Snippets
# Shift cypher

def encrypt(message, key):
    encrypted_message = []
    for char in message:
        s_char = ord(char) + key
        encrypted_message.append(chr(s_char))
    return ''.join(encrypted_message)

def encrypt(message, key):
    return ''.join(
        chr(ord(c) + key) for c in message
    )

