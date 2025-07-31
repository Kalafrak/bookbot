def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def characters_used(text):
    text_lower = text.lower()
    count = {}
    for char in text_lower:
        if char not in count:
            count[char] = 1
        else:
             count[char] += 1
    return count
