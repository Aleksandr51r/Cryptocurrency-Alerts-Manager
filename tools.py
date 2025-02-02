from random import choices
import string


def generate_unique_id(self, k=2):
    new_id = ''.join(choices(string.ascii_uppercase))
    return new_id
