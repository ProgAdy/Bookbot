def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        word_number = word_count(file_contents)
        letter_number = letter_count (file_contents)
        print (f"{word_number} words")
        print (letter_number)

def word_count(file_contents):
    words = file_contents.split()
    count_words=0
    for number_of_words in words:
        count_words += 1
    return count_words

def letter_count(file_contents):
    letters_dic={

    }
    
    for letters in file_contents:
        letter = letters.lower()
        if letter.isalpha():
            if letter in letters_dic:
                
                letters_dic[letter] += 1
            else:
                
                letters_dic[letter]=1
            
    letter_list= list(letters_dic.items())
    def sort_on (letters_dic):
        return letters_dic[1]
    letter_list.sort(reverse=True, key=sort_on)
    
    return letter_list



            
        


            
            



if __name__ == "__main__":
    main()
