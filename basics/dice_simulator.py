from random import randint

win_count = 0
lose_count = 0

dice = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

while True:
    input('Press enter to 🎲Roll Dice')
    out = randint(1,6)
    print(f'🎲 => {dice[out -1]}')
    if out == 6:
        win_count +=1
    elif out ==1:
        lose_count +=1
    if win_count ==3:
        print("You win 👑")        
        break
    # elif win_count ==6:
    #     print('you win 😍')
    elif lose_count ==3:
        print('you lose 💀')
        break




