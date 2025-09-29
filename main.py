from stats import count_words, count_chars, sort_on, sort_chars, print_chars
import sys

if len(sys.argv) > 1:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    file_text = get_book_text(book_path)
    word_count = count_words(file_text)
    
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    dictionary_list = sort_chars(count_chars(file_text))
    
    print_chars(dictionary_list)
    print("============= END ===============")

main()