import getpass
import os, sys, hangedmanJPG

print('Selamat datang di Hanged man')
wrongAnsw = int(0)


while True:
    secretWord = getpass.getpass('Masukan kata Rahasia: ')
    if(len(secretWord) > 0):
        print('Kata tersimpan')
        scrWord = list(secretWord)
        hint = input('Masukan Hint: ')
        break

scrLen = len(scrWord)

os.system('cls' if os.name == 'nt' else 'clear')
word = list(scrWord)
arr = [' _ ']*(len(scrWord))



while wrongAnsw < 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('the Word are')
    print(arr)
    print('The hint is ' + hint)
    print('')
    hangedmanJPG.picture(wrongAnsw)
    user_input = input("Enter a character: ")[0]
    if user_input in word:
        arr[word.index(user_input)] = user_input
    else:
        wrongAnsw += 1
    print(arr)
    if(word == arr):
        print('you found the word')
        wrongAnsw += 10
        break
    if(wrongAnsw == 3):
        print('You failed')
        break
