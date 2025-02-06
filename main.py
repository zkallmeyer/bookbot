def count_words(contents):
    words = contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_chars(contents):

    char_dict = {}
    # make file contents all lowercase
    lowered_contents = contents.lower()

    # iterate over contents and count characters, storing in dictionary
    for char in lowered_contents:
        if (char in char_dict):
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def main():
    # open book file and store contents in file_contents variable
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # count the number of words in the file
    word_count = count_words(file_contents)
    print(word_count)

    # count each character in the file
    char_counts = count_chars(file_contents)
    print(char_counts)

main()