from stats import count_words
from stats import count_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    file_content = ""
    with open(path) as file:
        file_content = file.read()
    count_words(file_content)
    count_characters(file_content)
    print("============= END ===============")
main()
