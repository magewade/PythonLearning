letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
morse_alpabet = dict(zip(letters, morse))

input_str = list(input())
count = 0
for litera in input_str:
    for key in morse_alpabet:
        if key == litera.upper():
            print(morse_alpabet[key], end=' ')
            count += 1


for c in word:
    if c in mydict:
        print(mydict[c], end=' ')