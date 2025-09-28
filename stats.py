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