import sys
def sort_on(items):
    return items[1]

def get_num_words(book):
    with open(f"{book}") as f:
        char_count = {}
        file_contents = f.read()
        num_words = len(file_contents.split())
        for char in file_contents:
            new_char = char.lower()
            char_count[new_char] = char_count.get(new_char, 0) + 1
        print(f"Found {num_words} total words")
        # A thing I had to look up
        sorted_chars = sorted(char_count.items(), reverse=True, key=sort_on)

        for char, count in sorted_chars:
            if char.isalpha():
                print(f"{char}: {count}")
        

def main():
    get_num_words(sys.argv[1])

main()