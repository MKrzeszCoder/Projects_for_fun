import pyautogui
import time
import random


osoby=[["Dawid","Nazwisko1"],["Artur","Nazwisko2"],["Jan","Nazwisko3"]]


wiadomosci_wlasciwe=["Cześć! Życzę Ci miłego dnia pełnego radości!",
                     " Witaj! Niech Twój dzień będzie wspaniały i słoneczny!",
                      "Hej! Życzę Ci fantastycznego dnia pełnego sukcesów!",
                     "Siema! Niech Twój dzień będzie pełen uśmiechów!",
                     "Hej! Baw się dziś ekstra i ciesz się każdą chwilą!",
                     "Witaj! Niech Twój dzień będzie pełen energii i entuzjazmu!",
                     "Cześć! Życzę Ci pięknego dnia pełnego inspiracji!",
                     "Siema! Niech Twój dzień będzie taki jak Ty – wyjątkowy!",
                     "Hej! Życzę Ci spokojnego dnia wypełnionego miłością i szczęściem!",
                     "Witaj! Życzę Ci udanego dnia pełnego sukcesów i radości",
                     "!Hej! Niech Twój dzień będzie niesamowity i pełen pozytywnych zaskoczeń!",
                     "Cześć! Życzę Ci spokojnego dnia i odrobiny relaksu!",
                     "Witaj! Niech każda chwila dzisiaj będzie wyjątkowa!",
                     "Siema! Życzę Ci siły i energii na cały dzień!",
                     "Cześć! Niech Twój dzień będzie pełen uśmiechu i radości!",
                     "Hej! Życzę Ci pełnego sukcesów i spełnienia dnia!",
                     "Witaj! Życze ci dziś samych pozytywnych zaskoczeń życiem!",
                     "Cześć! Życzę Ci, aby dzisiaj wszystko poszło po Twojej myśli!"]

def wyszukuje(osoba, wiadomosc):###### funkcja wyszukująca poszczególne osoby oraz wpisujące wiadomość
    polish_characters = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']
    odpowiedniki=['a','c','e','l','n','o','s','x','z','A','C','E','L','N','O','S','X','Z']
    pyautogui.hotkey('ctrl','k')

    for literka in osoba[0]:
        if literka not in polish_characters:
            pyautogui.typewrite(literka)
        else:
            pyautogui.keyDown('altright')
            pyautogui.typewrite(odpowiedniki[polish_characters.index(literka)])
            pyautogui.keyUp('altright')

    pyautogui.typewrite(' ')

    for literka in osoba[1]:
        if literka not in polish_characters:
            pyautogui.typewrite(literka)
        else:
            pyautogui.keyDown('altright')
            pyautogui.typewrite(odpowiedniki[polish_characters.index(literka)])
            pyautogui.keyUp('altright')

    time.sleep(2)
    pyautogui.hotkey('ctrl', '1')
    time.sleep(2)
    for literka in wiadomosc:
        if literka not in polish_characters:
            pyautogui.typewrite(literka)
        else:
            pyautogui.keyDown('altright')
            pyautogui.typewrite(odpowiedniki[polish_characters.index(literka)])
            pyautogui.keyUp('altright')
    pyautogui.hotkey('enter')
    time.sleep(2)



def aktywacja_ms():
    time.sleep(2)
    pyautogui.hotkey('win')
    time.sleep(0.4)
    pyautogui.typewrite('messenger')
    time.sleep(0.2)
    pyautogui.hotkey('enter')
    time.sleep(3)

def dezaktywacja_ms():
    time.sleep(1)
    pyautogui.keyDown('altleft')
    pyautogui.hotkey('f4')
    pyautogui.keyUp('altleft')




#############################################################ą
aktywacja_ms()

for osoba in osoby:
    time.sleep(1)
    wyszukuje(osoba,random.choice(wiadomosci_wlasciwe))

dezaktywacja_ms()
