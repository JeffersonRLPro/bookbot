def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def get_char_count(text):
    low_case_text = text.lower()
    # create a dictionary
    char_dict = {}
    for char in low_case_text:
        # check if its in the dict
        if char in char_dict:
            # increment the value
            char_dict[char] += 1
        else:
            # if not in dict add it to dict
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    new_chars =[]
    for char in char_dict:
        tmp_dict = {}
        tmp_dict["char"] = char
        tmp_dict["num"] = char_dict[char]
        # append to the list
        new_chars.append(tmp_dict)
    # sort the list
    new_chars.sort(reverse = True, key = sort_on)
    return new_chars