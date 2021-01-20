#
#     Author: Pulsar
#     GitHub: https://github.com/Woodnet
#     Twitter: https://www.twitter.com/7Pulsar
#     Python-Version: 3.8.2
#     Used Code-Editor: VSCode
#     Creation-Date: 12021 (Holozän-) | 2021 (gregorianisch)
#
import os,random,sys 
from time import sleep
from colorama import Fore,init,Style 

#Farben
B = Style.BRIGHT
r = B + Fore.RED 
g = B + Fore.GREEN 
w = B + Fore.WHITE 
c = B + Fore.CYAN 
y = B + Fore.YELLOW
#

class AFFE:
    def __init__(self):
        self.anzahl_durchlauf = bücherei['daten']['anzahl_durchläufe']
        self.gesuchtes_wort = bücherei['daten']['gesuchtes_wort']
        self.zahlen = bücherei['daten']['zahlen']
        self.buchstaben = bücherei['daten']['buchstaben']
        self.BLATT = bücherei['BLATT']
    
    def schreiben(self):
        print("\n")
        for i in range(self.anzahl_durchlauf):
            geschrieben_zähler = i
            if (geschrieben_zähler == 0):
                geschrieben_zähler += 1
            buchstaben_liste_len = len(self.buchstaben)    
            buchstaben_liste_len -= 1
            auswahl = random.randint(0,buchstaben_liste_len)
            ausgewählter_buchstabe = self.buchstaben[auswahl]
            self.BLATT.append(ausgewählter_buchstabe)
            sys.stdout.write("\r ".join(ausgewählter_buchstabe))
            sys.stdout.flush()
            geschrieben = "".join(self.BLATT)
            if (self.gesuchtes_wort in geschrieben): 
                print("\n\n [+] Wort %s wurde geschrieben!"%(self.gesuchtes_wort))
                print(" [+] %s Buchstaben wurden eingetippt."%(geschrieben_zähler))
                break
            else:
                if (len(self.BLATT) > 10000):
                    for n in range(5000):
                        self.BLATT.remove(self.BLATT[n])
                    self.clear_window()
                    print(" {%s} [#] 5000 Buchstaben wurden entfernt"%(geschrieben_zähler))
            geschrieben_zähler += 1
            #sleep(0.03)
        self.BLATT.clear()

    def clear_window(self):
        try:
            os.system("cls")  # Windows -default
        except:
            os.system("clear")  # Linux OS

bücherei = {
    'BLATT': [],
    'daten': {
        'anzahl_durchläufe': "",
        'gesuchtes_wort': "",
        'zahlen': ["1","2","3","4","5","6","7","8","9","0"],
        'buchstaben': [
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z"
        ],
    },
}

if __name__ == '__main__':
    try:
        while True:
            anzahl_durchlauf = input("Anzahl maximale Durchläufe: ")
            if (anzahl_durchlauf == "0" or anzahl_durchlauf == "" or anzahl_durchlauf == " "):
                pass
            else:
                break
        if (anzahl_durchlauf == "infinitus"):
            bücherei['daten']['anzahl_durchläufe'] = 10000000000000000000000000000000000000000
        else:
            bücherei['daten']['anzahl_durchläufe'] = int(anzahl_durchlauf)
        ZAHLEN = bücherei['daten']['zahlen']
        while True:
            gesuchtes_wort = input("Gesuchtes Wort: ")
            if (gesuchtes_wort == "" or gesuchtes_wort == " " or gesuchtes_wort in ZAHLEN):
                pass
            else:
                break
        bücherei['daten']['gesuchtes_wort'] = gesuchtes_wort.lower()
        #
        affe = AFFE()
        affe.clear_window()
        affe.schreiben()
        #
    except KeyboardInterrupt:
        pass
    
    print("\n\n [#] Der Affe hat aufgehört zu schreiben.\n")
    input("$")
