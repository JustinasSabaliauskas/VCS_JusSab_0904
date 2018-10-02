import random
import sys
import time


wordList = open("file2.txt",'r')
listas = wordList.readlines()
hangman = open("Hangman.py","r")
pakara =hangman.readlines()



guess_word = []
secretWord = random.choice(listas)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage =[]


def change():

    for character in secretWord:
        guess_word.append("*")
    time.sleep(2)
    print "Padesiu tau \n"
    time.sleep(2)
    print"Zodi kuri speliosi sudaro", length_word, "simboliai"


    print(guess_word)


def guessing():
    guess_taken = 3

    while guess_taken < 6:

        guess = raw_input("Pasirink raide:\n").lower()
        time.sleep(2)
        if not guess in alphabet:
            print("Zioply, ivesk raide nuo A iki Z")
        elif guess in letter_storage:
            print("Tokia raide jau spejai!!!!!")
        else:
            letter_storage.append(guess)
            if guess in secretWord:
                print("Oh, spejimas Teisingas!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '*' in guess_word:
                    print("Laimejai!")
                    break
            else:
                print("Tokios raides zodyje nera, bandyk dar karta!")
                guess_taken += 1
                if guess_taken == 10:
                    time.sleep(2)
                    print" Pralaimejai, zodis, kuri turejai atspeti buvo", secretWord.strip('\n')


change()
guessing()

print "Galas tau!!!!"
