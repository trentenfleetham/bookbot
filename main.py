def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    letters_list = character_list(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    # prints each character and number count line by line
    for item in letters_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

# key function - tells the sort function how to sort in the 'character_list' function.
def sort_on(d):
    return d["num"]

# converts 'character_dictionary' into a sorted list using 'sort_on' function above as the key and defining the letters as char and the numbers as num.
def character_list(character_dictionary):
    sorted_list = []
    for char in character_dictionary:
        sorted_list.append({"char": char, "num": character_dictionary[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# Finds and returns the count of each letter in a dictionary 'letter_count'
def get_num_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

# Splits the text into individual words and returns the count (length)
def get_num_words(text):
    words = text.split()
    return len(words)

# Uses defined book path to read the contents into a string 
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()