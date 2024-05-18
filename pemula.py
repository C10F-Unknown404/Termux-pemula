import os
import time

def clear_screen():
    os.system("clear")
    
    os.system("pkg install figlet")
 
def print_sasuke_logo():
    logo = """  ⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⣤⣤⣴⣶⣶⣦⣤⣤⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣉⣹⣿⣿⣿⣿⣏⣉⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⣠⣄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⣠⣄
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿
⠻⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠻⠟
⠀⠀⠀⠀⠉⠉⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀
[ author = android attack ]
[ sistem = online         ]
[ member = 110            ]
[ sc install bahan termux ]
=========================================================
"""
    print(logo)

print("menginstall bahan bahan termux")
print("harap koneksi cepet agar tidak fatal")
print("sistem berjalan")
print("loading...")
time.sleep(4)

commands = [
    "pkg install figlet -y",
    "pkg update -y",
    "pkg upgrade -y",
    "pkg install python -y",
    "pkg install python2 -y",
    "pkg install python3 -y",
    "pkg install ruby -y",
    "pkg install git -y",
    "pkg install php -y",
    "pkg install java -y",
    "pkg install perl -y",  # corrected from "parl"
    "pkg install nmap -y",
    "pkg install bash -y",
    "pkg install clang -y",
    "pkg install macchanger -y",
    "pkg install nano -y",
    "pkg install cowsay -y",
    "pkg install curl -y",
    "pkg install zip -y",
    "pkg install unzip -y",
    "pkg install tor -y",
    "pkg install sudo -y",
    "pkg install wget -y",
    "pkg install openssh -y",
    "pkg install bmon -y"
]

for command in commands:
    os.system(command)

print("\33[36;1mTerima kasih sudah menggunakan tools receh ini")