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

def main():
    file_contents = open_file("books/frankenstein.txt")

    print("---BEGIN REPORT---")
    print(str(count_words(file_contents)) + " words found in the document")

    character_count = count_characters(file_contents)

    for char_key in character_count:
        print("The character " + char_key + " was found " + str(character_count[char_key]) + " times")

    print("---END REPORT---")

main()
