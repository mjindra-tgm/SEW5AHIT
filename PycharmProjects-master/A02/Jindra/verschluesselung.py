3import threading
from random import randint


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Encryption(threading.Thread):
    """
    A Thread Class, to encrypt words, or wordparts
    """

    key = ""
    encrypt = ""
    decrypt =""

    dict = ["mnbvcxylkjhgfdsapoiuztrewq","qwertzuiopasdfghjklyxcvbnm","poiuztrewqasdfghjklmnbvcxy"]
    dictb = ["MNBVCXYLKJHGFDSAPOIUZTREWQ","QWERTZUIOPASDFGHJKLYXCVBNM","POIUZTREWQASDFGHJKLMNBVCXY"]
    dictc = ["1234567890!§$%&/()=?,.-#+´;:_'*", "*'_:;1234567890=)(/&%$§!+*#?,.-", ",.-#+0987654321?=)(/&%$§!;:_*'"]



    def __init__(self, word, key):
        """
        Constructor
        :param word: the word to translate
        """
        threading.Thread.__init__(self)
        self.word = word
        self.i=key

    def run(self):
        """
        Just the run
        :return:
        """
        if(self.i==-1):
            self.__enc()
        else:
            self.__dec()


    def __dec(self):
        """
        This method derypts words or wordparts
        :return:
        """

        for letter in self.word:
            if letter == " ":
                Encryption.decrypt += " "
            elif 64 < ord(letter) < 91:
                let = Encryption.dict[self.i].index(letter)+65
                Encryption.decrypt+=chr(let)
            elif 96 < ord(letter) < 123:
                let = Encryption.dict[self.i].index(letter) + 97
                Encryption.decrypt +=chr(let)
            elif 31 < ord(letter) < 64:
                let = Encryption.dict[self.i].index(letter) + 31
                Encryption.decrypt +=chr(let)

        Encryption.key += str(self.i);


    def __enc(self):
        """
        This method encrypts words or wordparts
        :return:
        """
        self.i = randint(0,len(self.dictb)-1)
        for letter in self.word:
            if letter==" ":
                Encryption.encrypt += " "
            elif 64 < ord(letter) < 91:
                Encryption.encrypt += Encryption.dictb[self.i][ord(letter)-65]
            elif 96 < ord(letter) < 123:
                Encryption.encrypt += Encryption.dict[self.i][ord(letter)-97]
            elif 31 < ord(letter) < 64:
                Encryption.encrypt += Encryption.dictc[self.i][ord(letter) - 31]
        Encryption.key+=str(self.i);


#Class end



def encrypt(word, number):
    """
    This method splits the word, and transfers them to different threads
    :param word: the word to encrypt
    :param number: the amount of threads, that are used, to encrypt the message
    :return:
    """
    zahl = round(len(word) / number)
    if zahl<1:
        print("Die Anzahl der Threads ist zu groß. Wir nehmen die maximal mögliche Anzahl an Threads")
        zahl=1
        number=len(word)
    for i in range(0, number):
        if i<number-1:
            thread = Encryption(word[i*zahl:(i+1)*zahl],-1)
        else:
            thread = Encryption(word[i * zahl:],-1)
        # Thread gleich starten
        thread.start()
    print(Encryption.encrypt)
    print("Key: "+Encryption.key)


def decrypt(word,key):
    """
    This methods splits the encrypted word to the end of the key, because every Part is encrypted with his own key
    :param word: word to decrypt
    :param key: key to decrypt the word
    :return:
    """
    number=len(key)
    zahl = round(len(word) / number)
    for i in range(0, number):
        if i<number-1:
            thread = Encryption(word[i*zahl:(i+1)*zahl],int(key[i]))
        else:
            thread = Encryption(word[i * zahl:],int(key[i]))
        # Thread gleich starten
        thread.start()
    print(Encryption.decrypt)

def all():
    """
    All is a method to combine all methods
    """
    encdec = input("Encrypt(enc) or Decrypt(dec):")
    while not (encdec == "enc" or encdec == "dec"):
        print(colors.WARNING+"Kein valider Wert"+colors.ENDC)
        encdec = input("Encrypt(enc) or Decrypt(dec):")

    message=input("Message: ")

    if encdec == "enc":
        number = input("Anzahl Threads: ")
        try:
            number = int(number)
        except ValueError:
            print(colors.WARNING+ number + " ist keine Zahl. Standardvariante wird durchgeführt. Ein Thread wird verwendet"+colors.ENDC)
            number = 1
        encrypt(message, number)
        return

    elif encdec == "dec":
        key = input("Key:")
        if key.isnumeric():
            if(len(key)>len(message)):
                print(colors.FAIL+"Ein Schlüssel kann nicht länger sein als das Wort"+colors.ENDC)

            else:
                decrypt(message,key)
                return
        else:
            print(colors.FAIL+"Dies ist kein Schlüssel"+colors.ENDC)
    all()

all()