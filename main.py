import sys

from stats import get_num_words, characters_used, chars_dict_to_sorted_list

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: File '{path_to_file}' not found")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied reading '{path_to_file}'")
        sys.exit(1)        

def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = get_num_words(file_contents)
    characters = characters_used(file_contents)
    sorted_char_count = chars_dict_to_sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sorted_char_count)
    print("============= END ===============")


if __name__ == "__main__":
    main()


