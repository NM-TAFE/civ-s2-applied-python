class Letter:
    def read_letter(self):
        return "I am unencrypted"

class EncryptedLetter(Letter):
    def decrypt_letter(self):
        return "I am encrypted"

letters = [Letter(), Letter(), EncryptedLetter(), Letter()]
for letter in letters:
    if isinstance(letter, EncryptedLetter):
        print(letter.decrypt_letter())
    else:
        print(letter.read_letter())
    if hasattr(letter, 'decrypt_letter'):
        print(letter.decrypt_letter())
    else:
        print(letter.read_letter())
