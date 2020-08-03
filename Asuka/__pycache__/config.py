import time
enemyAmount = "value"
Life = "value"
print("Hello user, welcome to config screen.")
time.sleep(0.6)
print("Please configure the game as you wish.")
time.sleep(0.5)
while True:
    enemyAmount = input("Enemy amount in game (Recommanded 50 < x < 200): ")
    try:
        val = int(enemyAmount)
    except ValueError:
        print("That's not a number!")
    else:
        if int(enemyAmount) < 0:
            print("Anti-Matter much?")
            time.sleep(0.4)
            pass
        else:
            break
while True:
    Life = input("Amount of life (Recommanded 3): ")
    try:
        val = int(Life)
    except ValueError:
        print("That's not a number!")
    else:
        if int(Life) < 0:
            print("Some people are living, but they are already dead...")
            time.sleep(0.4)
            pass
        else:
            break
while True:
    enemyMaxSpeed = input("Max Enemy Speed (Recommanded x > 8): ")
    try:
        val = int(enemyMaxSpeed)
    except ValueError:
        print("That's not a number!")
    else:
        if int(enemyMaxSpeed) < 0:
            print("enemyBackword.py aren't installed, file unsupported.")
            time.sleep(0.4)
            pass
        else:
            break
enemyAmount = int(enemyAmount)
Life = int(Life)
enemyMaxSpeed = int(enemyMaxSpeed)
initLife = int(Life)
