def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_count = {}

    for character in text:
        char = character.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

def sort_on(items):
    return items["num"]

def sorted_chars_list(text):
    unsorted_chars = get_num_chars(text)
    sorted_chars = []

    for character in unsorted_chars:
        temp_dict = {}
        temp_dict["char"] = character
        temp_dict["num"] = unsorted_chars[character]
        sorted_chars.append(temp_dict)
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars
