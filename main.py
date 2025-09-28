from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    file_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(file_text)
    char_count = count_chars(file_text)
    print(f"Found {word_count} total words")
    print(char_count)

main()