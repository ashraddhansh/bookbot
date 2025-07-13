from stats import get_char_count, get_word_count, get_word_list , get_book_text, get_char_dict, get_sorted_list


def main():
    # num_words = get_word_count(get_word_list(get_book_text("./books/frankenstein.txt")))
    # print(f"{num_words} words found in the document")
    # get_char_dict()
    get_sorted_list(get_char_dict())

main()
