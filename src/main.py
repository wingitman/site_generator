from textnode import TextNode


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print("Words: ", len(words))
        print(count_characters(file_contents))


def count_characters(txt):
    chars = {}
    for c in txt.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars


if __name__ == "__main__":
    main()
