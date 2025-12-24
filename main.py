def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words, get_num_chars, sorted_chars_list

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted = sorted_chars_list(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_set in sorted:
        character = char_set["char"]
        if character.isalpha():
            print(f"{char_set["char"]}: {char_set["num"]}")
    print("============= END ===============")

main()