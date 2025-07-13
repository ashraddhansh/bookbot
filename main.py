from stats import get_char_count, get_word_count, get_word_list , get_book_text, get_char_dict, get_sorted_list
import sys


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    else:
        
        bookPath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookPath}...")
        print("----------- Word Count ----------")
        num_words = get_word_count(get_word_list(get_book_text(bookPath)))
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        sorted_list = get_sorted_list(get_char_dict(bookPath))

        for i in sorted_list:
            key = i["char"]
            value = i["num"]
            print(f"{key}: {value}")




main() 
