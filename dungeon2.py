import random
import time
import sys

global name

def vardas():
    print"Sveikas atvykes i isbandymu labirinta\n"
    time.sleep(2)
    while True:
        name = ''
        name = raw_input ("Koks tavo varda:\n")
        if name == " ":
            time.sleep(2)
            print"Nieko neivedei. Gal tu durnas?"
        else:
            break
    return name

name = vardas()



def display():
    print "Sveiki,", name
    time.sleep(2)
    print" Atvykote i misliu shali. Tavo sprendimai, lems ateiti!"
    time.sleep(2)
    print " Turi 2 pasirinkimus. Viena kelia pasirinkes gal mirsi, kita misle minsi"
    time.sleep(2)

print()

display()

def chooseAnswer():
    answer = ""
    while answer != "1"  and answer != "2":
        print "Kuri kelia renkiesi,", name, ", 1 ar 2 ?"
        answer = raw_input()
    return answer

def checkAnswer(chosenAnswer):
    print" Pasirinkimas priimtas"
    time.sleep(2)
    print "Aplinkui viskas nutyla ir aptemsta..."
    time.sleep(2)
    print "Tamsus seselis isnyra is zemes ir taria:..."

    time.sleep(2)
    friendlyAnswer = random.randint(1, 2)

    if chosenAnswer == str(friendlyAnswer):
        print "Tau pasiseke, varguoli, siandien liksi gyvas!!!"
    else:
        print "Siandien ne tavo diena, Zaisim sunku zaidima!!!"
        from spelione import change
        return change()


restart = "taip"
while restart == "TAIP" or restart == "taip":

    answerNumber = chooseAnswer()

    checkAnswer(answerNumber)
    print("Jei nori bandyti savo sekme dar karta? Rasyk taip!")

    restart = raw_input()
else:
    print ("Greitai grizk, tikiu, dar pasimatysim!")
    sys.exit()