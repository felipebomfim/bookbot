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
    dictionaries = []
    for key, value in dictionary.items():
        dictionaries.append({'char': key, 'num': value})
    
    dictionaries.sort(reverse=True, key=lambda item: item["num"])
    return dictionaries