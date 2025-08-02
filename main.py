from stats import get_num_words
from stats import characters_used
from stats import sort_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(file_contents)
    characters = characters_used(file_contents)
    sorted_char_count = sort_characters(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

    


main()


