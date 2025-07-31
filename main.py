from stats import get_num_words
from stats import characters_used

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(file_contents)
    characters = characters_used(file_contents)
    print(f"{word_count} words found in the document")
    print(characters)


main()


