def count_words(file_text):
    print("----------- Word Count ----------")
    words = file_text.split()
    print(f"Found {len(words)} total words")

def sortNum(item):
    return item["num"]

def count_characters(file_text):
    print("--------- Character Count -------")
    char_count_dict = {}
    for raw_char in file_text:
        if raw_char.isspace():
            continue
        char = raw_char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    char_count_arr = []
    for char in char_count_dict:
        char_count_arr.append({"char": char, "num": char_count_dict[char]})
    char_count_arr.sort(reverse=True, key=sortNum)
    for char_dict in char_count_arr:
        print(f"{char_dict['char']}: {char_dict['num']}")
