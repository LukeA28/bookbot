with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def words(script):
    word_list = script.split()
    return len(word_list)

def letter_dictionary(book_string):
    letter_dict = {}
    letter_arr = list(file_contents)
    for letter in letter_arr:
        low_letter = letter.lower()
        if letter_dict.get(low_letter):
            letter_dict[low_letter] += 1
        else:
            letter_dict[low_letter] = 1
    return letter_dict