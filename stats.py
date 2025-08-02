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

def sort_characters(chars):
    sorted_chars = []
    for char, count in chars.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(reverse=True, key=lambda count: count["num"])        
    return sorted_chars        
