import random 
import os 

# Range ko 1 se 4 kar diya hai taaki 4 options ho sakein
num = random.randint(1, 4)
print(num)

os.system("clear")
print("\033[1m\033[33m[\033[32m---Booting--\033[33m]\033[0m")

# Condition 
if num == 1:
    os.system("mpv Access-Granted.mp3")
elif num == 2:
    os.system("mpv Jarvis2.mp3")
elif num == 3:
    os.system("mpv Ram.mp3")
else:
    # Yahan apna naya music file ka naam likhein
    os.system("mpv Mahadev.mp3")
