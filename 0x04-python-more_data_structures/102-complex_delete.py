#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return

    return {key: val for key, val in a_dictionary.items() if val != value}
