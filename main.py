import sys
from stats import get_number_of_words, get_dictionary_of_characters, get_sorted_dictionaries

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    # file_path = 'books/frankenstein.txt'

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)

    number_of_words_in_book = get_number_of_words(book_text)

    dictionary_of_characters = get_dictionary_of_characters(book_text)

    sorted_characters = get_sorted_dictionaries(dictionary_of_characters)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {file_path}...')
    print("----------- Word Count ----------")
    print(f'Found {number_of_words_in_book} total words')
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character['char'].isalpha():
            print(f'{character["char"]}: {character["num"]}')
            
    print("============== END ==============")

main()