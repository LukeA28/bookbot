def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    file_text = get_book_text("books/frankenstein.txt")
    print(file_text)

main()