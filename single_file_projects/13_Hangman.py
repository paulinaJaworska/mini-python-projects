import random


def main():

    capitals = ['Tirana', 'Andorra la Vella', 'Vienna', 'Minsk', 'Brussels', 'Sarajevo', 'Sofia', 'Zagreb', 'Nicosia', 'Prague',
                'Copenhagen', 'Tallinn', 'Helsinki', 'Paris', 'Berlin', 'Gibraltar', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome',
                'Pristina', 'Riga', 'Vaduz', 'Vilnius', 'Luxembourg', 'Skopje', 'Valletta', 'Monaco', 'Podgorica', 'Amsterdam', 'Oslo',
                'Warsaw', 'Lisbon', 'Bucharest', 'Moscow', 'San Marino', 'Belgrade', 'Bratislava', 'Ljubljana', 'Madrid', 'Stockholm',
                'Bern', 'Kiev', 'London', 'Vatican City']

    life_points = 5
    hidden_letters = []
    not_in_word = []
    word = ""

    def randomly_select_word():
        '''select word and transform it form the list into the string, so it looks better.'''
        word = ""
        random_word = str(random.sample(capitals, 1))
        random_word = random_word.lower()
        for i in range(2, len(random_word)-2):
            word += random_word[i]
            word.lower()
        return word

    def create_mutable_list_of_letters(word_to_guess):
        ''' Creates the list of letters, so it can be easlily modified. '''
        for i in range(0, len(word_to_guess)):
            if word_to_guess[i] != ' ':
                hidden_letters.append('_')
            else:
                hidden_letters.append(' ')
        return hidden_letters

    def decrease_life_points():  #vdef decrease_life_points(points):
        global life_points  # nic
        life_points -= 1
        print(life_points)
        if life_points == 0:
            print("You loose.")
        # return life_points, False   

    def display_dash_list(current_list):  # display_dash_list(current_list, points) do wywołania użyć display_dash_list(hidden_letters, life_points) # przy okazji wyświetla inne rzeczy
        ''' displays mutable_list_of letters with spaces between, so it looks like that: _ _ _ _ 
        Args:
            List
        Returns: 
            changed string of hidden letters, so if the letter 
            was guessed it shows this letter and the rest letters are hiden'''
        hidden_letters_to_display = ' '.join(hidden_letters)
        print(life_points)  # print(points)
        print(not_in_word)
        print(hidden_letters_to_display)  

    def take_input_from_player(word_to_guess, list_to_change):  # def take_input_from_player(word_to_guess, list_to_change, points):
        # take input form the player and put it into the dash list if a player guess is in the capital name to be guessed. 
        # Let the player to attempt the guess of whole name.
        while True:
            what_to_guess = str(input("Would you like to guess a letter (press l) or whole word(press w)? "))
            try:
                if what_to_guess == "l":
                    unhide_letter(word_to_guess, list_to_change)  # unhide_letter(word_to_guess, list_to_change, points)
                    return False
                if what_to_guess == "w":
                    check_if_player_guessed(word_to_guess)  # check_if_player_guessed(word_to_guess, points)
                else:
                    print("Your answer is not correct.")
                    decrease_life_points()    # decrease_life_points(points)
                    return False

                # else:    # jak to powinno być zapisane, albo jak to zapisać inaczej
                    # raise ValueError("'l' and 'w' are the only valid options to choose here.")

            except ValueError:
                print("'l' and 'w' are the only valid options to choose here.")
             #life_points return not_in_word, hidden_letters


    def unhide_letter(word_to_guess, list_to_change):   # unhide_letter(word_to_guess, list_to_change, points):
        # do wywołania: nhide_letter(word, hidden_letters, life_points)) ; word_to_guess == hidden_letters
        # list to change = hidden_letters_to_display     
        while True:    
            player_guess = str(input((("Please enter the letter: ").lower())))

            try:

                if player_guess in not_in_word:
                    print("This letter was already used. - 1 point.")
                    decrease_life_points()   # decrease_life_points(points) 
                    
                elif player_guess in word_to_guess:
                    print("Great!")
                    for letter in word_to_guess:
                        if letter == player_guess:  # czy i oznacza wartość kryjącą się pod kolejnym indexem czy sam index?
                            hidden_letters_to_display[i] = player_guess  # czy hidden_letters

                            # guessed_letters_positions.append(word_to_guess.index(i))
                            # for position in guessed_letters_positions:
                            # hidden_letters.insert(position, guess)
                        return False

                else:
                    print("Your answer is not corect")
                    decrease_life_points()  # decrease_life_points(points) 
                    # potem w main displa dash list
                return False

                return hidden_letters, # life_poins

            except ValueError:
                print("Only letters are valid input! Try again.")
                # guessed_letters_positions = []
                # if glayer_guess in word_to_guess:
                    
            # False # czemu zwraca false : do loop while w mainie. Może zadziała bez.

    def check_if_player_guessed(word_to_guess):   # check_if_player_guessed(word_to_guess, points):
        while True:
            player_guess = str(input("Please enter the capital name: "))
            player_guess = player_guess.lower()
            try:
                if player_guess == word_to_guess:   # czy będzie zgodność typów danych?
                    print("Fantastic! You got it right!")
                    print(f"Capital name: {word_to_guess}")
                    return False
                else:
                    print("Your answer is not corect")
                    decrease_life_points()  # decrease_life_points(points) 
        # czy chcę coś zwracać? MOże true albo false, żeby dac znać, że jest odgadnięte.
                #return life_points
            except ValueError:
                print("Words consist of letters!")
            
    word = randomly_select_word()
    print(word)  # check - delete later
    hidden_letters = create_mutable_list_of_letters(word)
    print(hidden_letters)  # check - delete later
    display_dash_list(hidden_letters) # display_dash_list(hidden_letters, life_points)
    take_input_from_player(word, hidden_letters)  # take_input_from_player(word, hidden_letters, life_points)
# while not hidden_letters == word:
#    create_mutable_list_of_letters(randomly_select_word())
#    take_input_from_player(randomly_select_word(), create_mutable_list_of_letters(word))

main()


def play_again():
    pass
















'''while True:   # opcja bez pytania czy litera czy słowo
player_guess = str(input("Please enter the letter or guess the word: "))
try:
    if len(player_guess) == 1:
        unhide_letter(player_guess)
    elif len(player_guess) == len(word_to_guess):
        check_if_player_guessed(player_guess, word_to_guess)
    else:
        print("Your answer is not correct.")
        decrease_life_points(life_points) #funkcja odejmująca punkty
except TypeError:
    print("Please enter one letter or your guess.")'''
