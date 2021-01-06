from random import randrange
import winsound

"""masaPuan = 0
pcPuan = 0
userPuan = 0


def oyun():
    global masaPuan
    global pcPuan
    global userPuan
    pc = 0
    masa = 0
    user = 0

    for x in range(10000):
        zar1 = randrange(1, 7)
        zar2 = randrange(1, 7)
        if zar2 < zar1:
            pc = pc + 1
        elif zar1 < zar2:
            user = user + 1
        else:
            masa = masa + 1

    print("KULLANICI: {}, PC: {}, MASA: {}".format(user, pc, masa))
    masaPuan = masaPuan + masa
    pcPuan = pcPuan + pc
    userPuan = userPuan + user


for i in range(10000):
    print("{}. oyun:".format(i+1))
    oyun()

print("NİHAİ SONUÇ\nMASA: {}\nKULLANICI: {}\nPC: {}".format(masaPuan, userPuan, pcPuan))

if masaPuan > userPuan and masaPuan > pcPuan:
    print("Masa Kazandı")
    winsound.Beep(frequency, duration)
elif masaPuan < userPuan and userPuan > pcPuan:
    print("Kullanıcı Kazandı")
    winsound.Beep(frequency, duration)
elif pcPuan > userPuan and pcPuan > masaPuan:
    print("Bilgisayar Kazandı")
    winsound.Beep(frequency, duration)"""

bahadirPuan = 0
onurPuan = 0

def bahadir():

    global onurPuan
    global bahadirPuan

    giris = input("Bahadır, aklımdan tuttuğum sayı kaç? > ")
    if int(giris) > 10:
        print("DÜZGÜN SAYI GİR")
    else:
        sayi = randrange(1, 11)

        giris = int(giris)

        if giris == sayi:
            print("DOĞRU!")
            winsound.Beep(2000, 1000)
            bahadirPuan = bahadirPuan + 1
            print("ONUR : " + str(onurPuan))
            print("BAHADIR: " + str(bahadirPuan))
            bahadir()
        else:
            print("YANLIŞ! SAYI {} İDİ".format(sayi))
            winsound.Beep(1000, 1000)
            onur()


def onur():

    global onurPuan
    global bahadirPuan

    giris = input("Onur, aklımdan tuttuğum sayı kaç? > ")
    if int(giris) > 10:
        print("DÜZGÜN SAYI GİR")
    else:
        sayi = randrange(1, 11)

        giris = int(giris)

        if giris == sayi:
            print("DOĞRU!")
            winsound.Beep(2000, 1000)
            onurPuan = onurPuan + 1
            print("ONUR : " + str(onurPuan))
            print("BAHADIR: " + str(bahadirPuan))
            onur()
        else:
            print("YANLIŞ! SAYI {} İDİ".format(sayi))
            winsound.Beep(1000, 1000)
            bahadir()



while (1):
    bahadir()
