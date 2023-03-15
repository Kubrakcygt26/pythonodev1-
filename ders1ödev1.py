# Python'da Veri tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklama yapınız. 
# string (metin) veri tipleri = str 

# numerik(sayısal) veri tipleri = int,float,complex 

# sequence(sıralama) veri tipleri = list,tuple,range 

# mapping(haritalama) veri tipleri = dict 

# set veri tipleri = set,frozenset 

# boolean veri tipleri = bool 

# binary veri tipleri = bytes,bytearray, memoryview 

# # Örnekler 
# a ="Merhaba"                                   (str)
# b = 63                                         (int)
# c = 64.4                                       (float)
# d = 67j                                        (complex)
# e = ["Domates","Biber","Patlıcan"]             (list)
# f = ("Domates","Biber","Patlıcan")             (tuple)
# g = range(4)                                   (range)
# h = {"adı" : "Ayşe","yaşı" : 58}               (dict)
# i ={"Ayça","Hasan","Tuğba"}                    (set)
# j = frozenset({"Domates","Biber","Patlıcan"})  (frozenset)
# k = True                                       (bool)
# l = b"Merhaba"                                 (bytes)
# m = bytearray(8)                               (bytearray)
# n = memoryview(bytes(4))                       (memoryview)

# Kodlama.io sistesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
# 2023 Yazılım Geliştirici Yetiştirme Kampı- Python & Selenium, Ders Programı, Ödev 1 ve Ödev 2 string veri tiplerine örnektir. 
# Tamamlama yüzdesi numeric(int) örneğidir. 
# Eğitmen list örneğidir. 

# Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
kullanici = "pythonlearner"
şifre = "1234"

print("Kullanici adinizi giriniz: ")
a = str(input());

print("Sifrenizi giriniz: ")
b = str(input());

if kullanici == a and şifre == b:
    print("--Giris yapilmistir--")
elif user! = a or password! =b:
    print("**Kullanici adi veya sifre hatali**")
