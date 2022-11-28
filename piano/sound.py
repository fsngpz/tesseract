import os

def start():
    # list = input("masukkan not angka:")
    # arrList = list.split(" ")
    arrList = []
    print(arrList)

    for x in arrList:
        play(x)


def play(not_angka):
    if not_angka == "1":
        file = 'normal/C.wav'
        os.system("afplay " + file)
    elif not_angka == "2":
        file = 'normal/D.wav'
        os.system("afplay " + file)
    elif not_angka == "3":
        file = 'normal/E.wav'
        os.system("afplay " + file)
    elif not_angka == "4":
        file = 'normal/F.wav'
        os.system("afplay " + file)
    elif not_angka == "5":
        file = 'normal/G.wav'
        os.system("afplay " + file)
    elif not_angka == "6":
        file = 'normal/A.wav'
        os.system("afplay " + file)
    elif not_angka == "7":
        file = 'normal/B.wav'
        os.system("afplay " + file)
    elif not_angka == "8":
        file = 'normal/Cc.wav'
        os.system("afplay " + file)


if __name__ == '__main__':
    start()
