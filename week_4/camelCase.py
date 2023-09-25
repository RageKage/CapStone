import string 

def camel_case(Sentence):
    if Sentence.isspace() or Sentence == "":
        return ""
    split_string = Sentence.split()
    
    for i in range(len(split_string)):
        
        for j in range(len(split_string[i])):
                if split_string[i][j] in string.punctuation :
                    return ""
                if split_string[i][j].isdigit():
                    return ""
        split_string[i] = split_string[i].capitalize()
    
    split_string[0] = split_string[0].lower()
    
    Camel = "".join(split_string)
    
    return Camel
    
def main():
    Sentence = input("Enter a sentence: ")
    camelcased = camel_case(Sentence)
    print(camelcased)
    

if __name__ == "__main__":
    main()