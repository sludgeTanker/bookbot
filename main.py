def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("\n")
    get_character_count(text)
    print("--- End report ---")


def get_character_count(text):
    text = text.lower()
    character_count = {}
    character_count = set(text)
    character_count = dict.fromkeys(character_count, 0)
    for character in text:
        character_count[character] += 1
    def sort_on(dict):
        return dict["num"]
    new_characters = [{"character": char, "num": num} for char, num in character_count.items()]
    new_characters.sort(reverse=True, key=sort_on)
    for item in new_characters:
        if item['character'].isalpha():
            print(f"The '{item['character']}' character was found {item['num']} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()