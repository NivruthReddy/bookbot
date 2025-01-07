def main():
    print("--- Begin report of books/frankenstein.txt ---")
    count_words()
    all_chars_dict = count_characters()
    report_time = count_alphabets(all_chars_dict)
    generate_report(report_time)
    print("--- End report ---")
def read_file():
    with open("books/frankenstein.txt") as f:
        read_contents = f.read()
        return read_contents

def count_words():
    file_contents = read_file()
    #Removing Newlines from the text
    lines = file_contents.split('\n')     
    full_string = ""
    #Joining back the text as a single string, with spaces in between after each iteration
    for line in lines:
        full_string = full_string + " " + line
    #Splitting the single string into seperate words without spaces    
    words_with_no_spaces = full_string.split(' ')
    onlyWords = []
    for word in words_with_no_spaces:
        if word != '':
            onlyWords.append(word)
    #Printing the number of words        
    print(f"{len(onlyWords)} words found in the document \n\n")

def count_characters():
    contents_file = read_file()
    lowercase_file = contents_file.lower()
    #Creating an empty dictionary    
    track_count = dict()
    #Checking whether the element is present in the newly made dictionary and tracking the count accordingly
    for letter in lowercase_file:
        if letter not in track_count:
            track_count[letter] = 1
        else:   
            track_count[letter] = track_count[letter] + 1
    return track_count

def count_alphabets(dictionary):
    #Making a dictionary where only alphabets are contained
    alphabets_only = dict()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for key in dictionary:
        if(key in alphabets):
            alphabets_only[key] = dictionary[key]
    return alphabets_only        


def generate_report(report_generate):
    empty_list = []
    for keyy in report_generate:
        empty_list.append((report_generate[keyy], keyy))

    empty_list.sort(reverse = True)
    
    for element in empty_list:
        print(f"The '{element[1]}' character was found {element[0]} times")


main()   
