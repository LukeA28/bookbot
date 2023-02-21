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

def sort_results(dict):
    origin_list = list(dict.items())
    order_list = list()
    highest = 0
    while origin_list:
        for pair in origin_list:
            if pair[0].isalpha():
                if pair[1] > highest:
                    highest = pair[1]
            else:
                origin_list.remove(pair)
        for couple in origin_list:
            if couple[1] == highest:
                order_list.append(couple)
                origin_list.remove(couple)
        highest = 0
    return order_list

def print_report(letter_list):
    print(f"--- Begin report of {f.name} ---")
    print(f"{words(file_contents)} words found in the document\n")
    for letter in letter_list:
        print(f"The {letter[0]} character was found {letter[1]} times")
    print("--- End report ---")


print_report(sort_results(letter_dictionary(file_contents)))
