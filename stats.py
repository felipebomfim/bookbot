def get_number_of_words(string):
    return len(string.split())

def get_dictionary_of_characters(string):
    characters = {}
    for char in string:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def get_sorted_dictionaries(dictionary):
    sorted_by_value = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    sorted_dictionaries = []
    for key, value in sorted_by_value.items():
        sorted_dictionaries.append({'char': key, 'num': value})
    return sorted_dictionaries