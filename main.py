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


# returns the count of each character for sorting
def sort_chars(char_dict):
    return char_dict["count"]


# splits the character counts up for sorting purposes
def convert_dict_to_list(char_dict):
    alpha_char_counts = []
    # for each character in the dict
    for c in char_dict:
        # only include characters from the alphabet
        if (c.isalpha()):
            count = char_dict[c]
            # add kry-value pair to list
            pair = {"char": c, "count": count}
            alpha_char_counts.append(pair)
    return alpha_char_counts

# print formatted report
def print_report(words, sorted_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for c in sorted_chars:
        print(f"The '{c["char"]}' character was found {c["count"]} times")
    print("--- End report ---")




book_path = "books/frankenstein.txt"

def main():
    # open book file and store contents in file_contents variable
    with open(book_path) as f:
        file_contents = f.read()
    
    # count the number of words in the file
    word_count = count_words(file_contents)

    # count each character in the file
    char_counts = count_chars(file_contents)
    
    # split up and sort character counts
    list_of_pairs = convert_dict_to_list(char_counts)
    list_of_pairs.sort(reverse=True, key=sort_chars)

    # generate report
    print_report(word_count, list_of_pairs)


main()