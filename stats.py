def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(fp):
    book = get_book_text(fp)
    words = book.split()
    num_words = len(words)
    return num_words

def get_num_characters(fp):
    book = get_book_text(fp)
    book_lower = book.lower()
    result = {}
    for character in book_lower:
        if character in result:
            result[character] = result[character] + 1
        else:
            result[character] = 1
    return result

def get_sorted_list(book_path, num_words, num_chars):
    pair_num_chars = []
    for pair in num_chars:
        if pair.isalpha():
            pair_num_chars.append({"name" : pair, "num" : num_chars[pair]})
    
    def sort_key(items):
        return items["num"]
    
    pair_num_chars.sort(reverse=True, key=sort_key)

    result_list = []
    for pair in pair_num_chars:
        result_list.append(f"{pair["name"]}: {pair["num"]}")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in result_list:
        print(pair)
    print("============= END ===============")