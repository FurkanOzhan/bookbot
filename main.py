def read_char_count(text):
    result = {}
    for char in text:
        c = char.lower()
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    # print(result)
    return result
    
def report_char_count(char_count):
    del char_count[' '] # remove space
    del char_count['.'] # remove dot
    del char_count['#'] # remove #

    s = {k: v for k, v in sorted(char_count.items(), key=lambda item: item[1], reverse=True)}
    
    for char, count in s.items():
        print(f"The '{char}' character was found {count} times")


def word_count(text):
    words = text.split()
    print(len(words) ," words found in the document \n")


def main():
    with open("./books/frankenstein.txt") as f:
        contents  = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        word_count(contents)
        char_counts = read_char_count(contents)
        report_char_count(char_counts)
        print("--- End report ---")
        


if __name__ == '__main__':
    main()