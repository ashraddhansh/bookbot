def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents # this will give the whole text in string format

def get_word_list(file_contents):
    split_content=file_contents.split()
    return split_content # this will print a list of words that are separated by space in the text

def get_word_count(word_list):
    return len(word_list)

def get_char_count(file_contents, char):
    lower_contents = file_contents.lower()
    word_count = lower_contents.count(char)
    
    return word_count

def get_char_dict(bookPath):
    count_dict = {}

    for i in range(ord('a'), ord('z') + 1):
        count = get_char_count(get_book_text(bookPath),chr(i))
        count_dict[chr(i)] = count
    return count_dict


def get_sorted_list(count_dict):
    unsorted_list = []
    for key in count_dict:
        char_dict = {}
        char_dict["char"] = key
        char_dict["num"] = count_dict[key]
        unsorted_list.append(char_dict)

    def sort_on(items):
        return items["num"]
    unsorted_list.sort(reverse = True, key = sort_on)
    return unsorted_list



