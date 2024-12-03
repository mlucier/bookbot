import string

def open_file(file_string):
    file_contents = ""

    with open(file_string) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    word_count = 0
    words = text.split();

    for word in words:
        word_count += 1

    return word_count

def count_characters(text):
    lowercase_dict = {}
    chars = list(text.lower())
    ascii_chars = list(string.ascii_lowercase)

    for char in chars:
        if char in ascii_chars:
            if char in lowercase_dict:
                lowercase_dict[char] += 1
            else:
                lowercase_dict[char] = 1

    return lowercase_dict

def sort_on(dict):
    return dict["count"]

def main():
    file_string = "books/frankenstein.txt"
    file_contents = open_file(file_string)

    print(f"--- Begin report of {file_string} ---")
    print(str(count_words(file_contents)) + " words found in the document")
    print("")

    character_count = count_characters(file_contents)
    character_count_list = []

    for key in character_count:
        character_count_list.append({"char": key, "count": character_count[key]})

    character_count_list.sort(reverse=True, key=sort_on)

    for char in character_count_list:
        print("The character '" + char["char"] + "' was found " + str(char["count"]) + " times")

    print("--- End report ---")

main()
