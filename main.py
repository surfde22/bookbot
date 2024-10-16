def main():
    book_path = "books/frankenstein.txt"
    book_text = read_file(book_path)
    num_words = word_count(book_text)
    char_dict = get_char_dict(book_text)
    char_sort = []
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    #print(char_dict)
    char_sort = pair_char_dict(char_dict)
    for char in char_sort:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    #print(char_sort)

def read_file(file_to_read):
    with open(file_to_read) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    lowered_text = text.lower()
    each_letter = {}
    for letter in lowered_text:
        if letter not in each_letter.keys():
            each_letter[letter] = 1
        else:
            each_letter[letter] += 1
    return each_letter

def sort_on(dict):
    return dict["count"]

def pair_char_dict(dict_char):
    new_char_list = []
    for char in dict_char:
        temp_dict = ""
        if char.isalpha():
            temp_dict = {"char": char, "count": dict_char[char]}
            new_char_list.append(temp_dict)
    new_char_list.sort(reverse=True, key=sort_on)
    return new_char_list

main()