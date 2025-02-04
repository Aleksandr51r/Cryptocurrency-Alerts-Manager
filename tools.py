from random import choices
import string


def generate_unique_id(k=2):
    new_id = ''.join(choices(string.ascii_uppercase, k=k))
    return new_id
