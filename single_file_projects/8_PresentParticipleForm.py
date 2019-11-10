import sys
def present_participle():
    # creates present participle form from the verb
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            try:

                word = str(item)
                consonants = ['B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', "j", 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', "S", 's', 'T', 't', 'V', 'v', 'X', 'x', 'Z', 'z']
                vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
            
                if word[-2:] == 'ie':
                    # converts words ending with ie
                    word = word[:-3]
                    print(str(word) + "ying")
                elif word[-1] == 'e' and word[-2] != 'e':
                    # converts words ending with e and exclude exceptions of words ending with double ee
                    word = word[:-1]
                    print(str(word) + "ing")
                elif len(word) == 3 and word[0] in consonants and word[1] in vowels and word[2] in consonants:
                    # converts words like consonant - vowel - consonant
                    word = word + word[-1]
                    print(str(word) + "ing")
                else:
                    # adds ing at the end of the argument for the rest of the worlds without converting them
                    print(str(word) + "ing")
            
            except ValueError:
                print("Please, enter words only!")
    else:
        print("Please, specify aruments.")

present_participle()

