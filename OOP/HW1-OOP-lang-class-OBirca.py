class English:
    name = 'English'
    alphabet = 'latin'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    total_words = 400_000

    dialects = [
        "British English",
        "American English",
        "Australian English",
        "Canadian English",
        "Indian English",
        "South African English",
        "Irish English",
        "Scottish English",
    ]
    
    
    def sayHi():
        print("Hello")

    def sayBye():
        print("Bye")


class Romanian:
    name = 'Romanian'
    alphabet = 'latin'
    letters = ['a', 'ă', 'â', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'ș', 't', 'ț', 'u', 'v', 'w', 'x', 'y', 'z']

    total_words = 175_000

    dialects = [
        "Moldavian Romanian",
        "Transylvanian Romanian",
        "Banat Romanian",
        "Muntenian Romanian",
        "Oltenian Romanian"
    ]
    
    
    def sayHi():
        print("Salut")

    def sayBye():
        print("Pa")
        

class Russian:
    name = 'Russian'
    alphabet = 'cyrilic'
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    total_words = 200_000

    dialects = [
        "Moscow Russian",
        "St. Petersburg Russian",
        "Southern Russian",
        "Siberian Russian",
        "Ural Russian",
        "Northern Russian"
    ]
    
    
    def sayHi():
        print("Привет")

    def sayBye():
        print("Пока")


list = [English, Romanian, Russian] 


#### show letters
def showLetters(list, l):
    for i in range(len(list[l].letters)):
        print (list[l].letters[i], end="")
        if i == len(list[l].letters)-1:
            print(".", end = " ")
        else: 
            print(",", end = " ")
        i += 1

    print()
    
#### show dialects

def showDialects(list, l):
    for i in range(len(list[l].dialects)):
        print ("  -", list[l].dialects[i], end="")
        if i == len(list[l].dialects)-1:
            print(".", end = " ")
        else: 
            print(",")
        i += 1

    print()




for i in range(len(list)):
    print (list[i].name, "is using a", list[i].alphabet, "alphabet having the letters: ")
    showLetters(list, i)
    print ("It has about", list[i].total_words, ". The most known dialects are" )
    showDialects(list, i)
    print()
