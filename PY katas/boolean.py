""""Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false."""

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

def bool_to_word(bool):
    return "Yes" if bool else "No"


def bool_to_word(bool):
     if bool:
         return "Yes"
     return "No"


def bool_to_word(bool):
    return ['No', 'Yes'][bool]
"""en python false est egal à 0 et true à 1"""