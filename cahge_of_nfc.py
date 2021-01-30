import unicodedata

import pyperclip as ppc


def change_of_nfc(donot_in: int):
    change_string = ppc.paste()
    changed_string = unicodedata.normalize('NFC', change_string)
    ppc.copy(changed_string)


if __name__ == '__main__':
    change_of_nfc(0)
