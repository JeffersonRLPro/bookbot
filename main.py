from stats import get_num_words, get_char_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])
    num = get_num_words(text)
    chars = get_char_count(text)
    ordered_chars = sort_dict(chars)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {num} total words\n--------- Character Count -------") 
    # loop through the list
    for item in ordered_chars:
        # check to see if char is letter
        if item["char"].isalpha():
            # print the char and the num
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

if len(sys.argv) < 2:
    # print message
    print("Usage: python3 main.py <path_to_book>")
    # exit
    sys.exit(1)
else:
    main()