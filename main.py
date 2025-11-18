import sys
from stats import get_num_words, get_num_characters, get_sorted_list

if len(sys.argv) == 2:
    def main():
        get_sorted_list(sys.argv[1], get_num_words(sys.argv[1]), get_num_characters(sys.argv[1]))
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
