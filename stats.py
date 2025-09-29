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

    for chrctr, num in char_dict.items():
        char_pair = {"char": chrctr, "num": num}
        dict_list.append(char_pair)
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_chars(char_list):
    for dict in char_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")