def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(text_str):
    words = text_str.split()
    return len(words)
    
def main():
    file_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(file_text)} total words")

main()