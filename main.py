
def main():
    
    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

    return file_contents

def count_words(file_contents):

    words = file_contents.split()
    return len(words), words

def count_char(words):

    char_dict = {}
    for char in words:
        char = char.lower()
        char_dict[char] = char_dict.get(char, 0)+1
    
    return char_dict

def sort_on(dict):
    return dict["count"]

def word_report(char_dict):

    count_list = []
    for char, count in char_dict.items():
        count_list.append({"char":char, "count":count})
    count_list.sort(reverse=True, key=sort_on)

    return count_list


if __name__ == "__main__":

    file_contents = main()
    count, words = count_words(file_contents)
    char_dict = count_char(file_contents)
    count_list = word_report(char_dict)
    print(count_list)
    for count in count_list:
        print(f"The '{count["char"]}' character was found {count["count"]} times")
    