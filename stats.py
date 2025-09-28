def count_words(text_str):
    words = text_str.split()
    return len(words)

def count_chars(book_text):
    text_chars = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char in text_chars:
            text_chars[char] += 1
        else:
            text_chars[char] = 1
    return text_chars

def sort_on(items):
    return items["num"]

def sort_chars(char_dict):
    dict_list = []
    char_pair = {}
    for chrctr in char_dict:
        char_pair["char"] = chrctr
        char_pair["num"] = char_dict[chrctr]
        dict_list.append(char_pair)
        char_pair.clear()
    return dict_list.sort(reverse=True, key=sort_on)