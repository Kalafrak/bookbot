def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    word_list = text.split()
    return len(word_list)
    

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(file_contents)
    print(f"{word_count} words found in the document")


main()


