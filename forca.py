def play():
    print("Welcome: Forca")
    
    word = "ch".strip().upper()
    word_hit = ["_" for letter in word ]

    hanged = False
    hit = False
    error = 0 
    lack_word = (word_hit.count('_'))

    print(word_hit)

    while(not hanged and not hit):

        guesses = input("What is your guesses? ")
        guesses = guesses.strip().upper()

        if guesses in word:
            index =0
            for letter in word:
                if(guesses == letter):
                    word_hit[index] = letter
                index = index + 1
            lack_word = str(word_hit.count('_'))                
            print("Still need hit {} letters" .format(lack_word))           
        else:
            error = error + 1
            print("Letter not found, you used {} tries out of {} " .format(error, len(word_hit)))

        hanged = error == len(word_hit)
        hit = "_" not in word_hit

        if hit:
            print("you win, congratulations!! the word was {}" .format(word))
            break
        elif hanged:
            print("you lost")
            break

        print(word_hit)

if(__name__ == "__main__"):
    play()

