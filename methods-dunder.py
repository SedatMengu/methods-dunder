# # dunder methods (magic methods)

# # python üzerinde daha önceden tanımlı ve görevi olan fonksiyonlardır.
# # __ ile başlayıp bitiyor olması onları tanımamıza yarar. double underscore kısaltmasıdır.

# print(int.__add__(3,5))
# print( 3 + 5 )               # / 8
# # bizim yazdığımız : print( 3 + 5 )  pythonun anladığı print(int.__add__(3,5))

# print("ali"+"veli")          # / aliveli
# # bizim yazdığımız : print("ali"+"veli")  pythonun anladığı print(str.__add__(qli,veli))

# print([1,2,3] + [4,5,6])     # / [1,2,3,4,5,6]
# # bizim yazdığımız : print([1,2,3] + [4,5,6])  pythonun anladığı print(list.__add__([1,2,3],[4,5,6]))

# print(int.__mul__(8,2))
# print(str.__mul__("Oğuz",7))
# print(list.__mul__([1,2,3],3))
# print(int.__sub__(6,4))

# class Mylist(list):             # list klasından miras alarak yeni bir class oluşturduk.
#     pass                        # pass geçtiğim için miras olarak aldığım list clasına ait bütün özellikler birebir kullanılacak.

# liste1 = Mylist([1,2,3])
# liste2 = Mylist([4,5,6])

# print(liste1 + liste2)          # / [1, 2, 3, 4, 5, 6]  listelerdeki standart dunder metot olarak list.__add__() çalıştı.

class Mylist1(list):                                    # list klasından miras alarak yeni bir class oluşturduk.
    def __add__(self,other):                            # standart olarak toplama yapmasın da benim ayarladığım gibi toplama yapsın diye kalıtım ile geleni ezecek bir dunder yazıyorum
        if len(self) != len(other):                     # self parametresi ile other listelerinin index sayıları farklı ise 
            return "listeler eşit uzunlukta değil"      # bu mesajı return et
        else:                                           # eğer değil ise
            result = Mylist1()                            # result adında boş bir liste türettik
            for i in range(len(self)):                  # self eleman sayısı kadar dönen bir döngü oluşturduk.
                result.append(self[i]+ other[i])        # asıl amacımız burada. self listesindeki eleman ile other listesindeki elemanı topla ve result listesinin içine gönder , bunu self listesi elemanları bitene kadar devam ettir.
        return result                                   # oluşan result listesini return et.


liste11 = Mylist1([1,2,3])                              # / yeni oluşturduğumuz class dan liste11 nesnesi oluşturduk
liste12 = Mylist1([4,5,6])                              # / yeni oluşturduğumuz class dan liste12 nesnesi oluşturduk.
liste13 = Mylist1([6,5,4,3])                            # / yeni oluşturduğumuz class dan liste13 nesnesi oluşturduk.

print(liste11 + liste12)                                # / eğer class içerisine toplama için herhangi bir fonksiyon yazmasaydık [1, 2, 3, 4, 5, 6] şeklinde bir ifade dönecekti , ancak biz Mylist1 classında + operatörünü görünce ne yapması gerektiğini bildirdiğimiz için kalıtım ile gelen list.__add__() fonksiyonunu almadı. onu ezdik.
print(liste11 + liste13)                                # / "listeler eşit uzunlukta değil" bunu biz ayarlamıştık.


# tanımlı olmayan bir fonksiyon da tanımlayabiliriz.


class Mylist2(list):                                    # list klasından miras alarak yeni bir class oluşturduk.
    def __sub__(self,other):                            # standart olarak toplama yapmasın da benim ayarladığım gibi toplama yapsın diye kalıtım ile geleni ezecek bir dunder yazıyorum
        if len(self) != len(other):                     # self parametresi ile other listelerinin index sayıları farklı ise 
            return "listeler eşit uzunlukta değil"      # bu mesajı return et
        else:                                           # eğer değil ise
            result = Mylist1()                            # result adında boş bir liste türettik
            for i in range(len(self)):                  # self eleman sayısı kadar dönen bir döngü oluşturduk.
                result.append(self[i] - other[i])        # asıl amacımız burada. self listesindeki eleman ile other listesindeki elemanı topla ve result listesinin içine gönder , bunu self listesi elemanları bitene kadar devam ettir.
        return result 


liste21 = Mylist2([1,2,3])                              # / yeni oluşturduğumuz class dan liste21 nesnesi oluşturduk
liste22 = Mylist2([4,5,6])                              # / yeni oluşturduğumuz class dan liste22 nesnesi oluşturduk.
liste23 = Mylist2([6,5,4,3])                            # / yeni oluşturduğumuz class dan liste23 nesnesi oluşturduk.

print(liste21 - liste22)                                # / [-3, -3, -3]
print(liste21 - liste23)                                # / listeler eşit uzunlukta değil


# liste elemanlarının toplamları eşişliğini kontrol eden bir fonksiyon yazacağz

class Mylist3(list):                                    # list klasından miras alarak yeni bir class oluşturduk.
    def __eq__(self,other):                             # miras yolu ile gelen eşit olup olmadığını kontrol eden fonksyionu ezeceğiz
        if sum(self) == sum(other):                     # self listesinin elemanları toplamı other listesinin elemanlarının toplamına eşit ise
            return True                                 # true döndür
        return False                                    # normalde else : yazmamız gerekiyordu ancak yazmasak da olur.


liste31 = Mylist3([1,2,3])                              # / yeni oluşturduğumuz class dan liste31 nesnesi oluşturduk
liste32 = Mylist3([4,5,6])                              # / yeni oluşturduğumuz class dan liste32 nesnesi oluşturduk.
liste33 = Mylist3([6,5,4,3])                            # / yeni oluşturduğumuz class dan liste33 nesnesi oluşturduk.

print(liste31 == liste32)                               # / False ,  == operatörüne ne yapması gerektiğiniz oluşturduğumuz class içerisinde tanımladığımızdan kalıtım ile gelen davranış devre dışı kaldı. sonuç false


# listedeki negatif değerleri pozitif yapan bir fonksiyon yapacağız

class Mylist4(list):                                    # list klasından miras alarak yeni bir class oluşturduk.
    def __abs__(self):                                  # miras yolu ile gelmeyen mutlak değer fonksiyonunu kendimiz oluşturacağız
        result = Mylist4()                              # çıktı için Mylist4 den türetilen boş bir liste oluşturduk.
        for i in self:                                  # self elemanları içerisinde bir döngü oluşturduk,
            if i>=0:                                    # eğer i elemanı sıfırdan büyük ise
                result.append(i)                        # i elemanını daha önce oluşturduğumuz result listesinin sonuna ekle,
            else:
                result.append(-1 * i)                   # eğer - işaretli ise -1 ile çarpıp listenin sonuna ekle dedik.
        return result

liste41 = Mylist4([1,2,-3])                              # / yeni oluşturduğumuz class dan liste31 nesnesi oluşturduk
liste42 = Mylist4([4,-5,6])                              # / yeni oluşturduğumuz class dan liste32 nesnesi oluşturduk.
liste43 = Mylist4([-6,5,4,-3])                           # / yeni oluşturduğumuz class dan liste33 nesnesi oluşturduk.

print(abs(liste41))                                      # / [1, 2, 3] listede fonksiyonları içerisinde bulunmayan abs adında bir fonksiyon tanımladık ve kullandık. negatif değerleri pozitif yaptı.


# herhangi bir yerden miras almayan bir class oluşturalım

class futbolcu:                                                         # / kalıtım yolu ile herhangi bir miras almayan bir sınıf türettik
    def __init__(self,isim,soyisim,yas):                                # bu classda isim , soyisim , yas değişkenleri var
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas
    def __eq__(self,other):                                             # iki oyuncunun adı , soyadı eşit ise futbolcu eşittir dicez.
        if self.isim == other.isim and self.soyisim == other.soyisim:   
            return True
        return False
    
    def __add__(self,other):                                        # toplama fonksiyonunu kendimize göre uyarladık.
        isim =self.isim[0] + other.isim[0]                          # isimlerin ilk harflerinden bir isim değişkeni oluşturduk
        soyisim=self.soyisim[0] + other.soyisim[0]                  # soyisimlerin ilk harflerinden bir soyisim değişkeni oluşturuduk
        yas= self.yas + other.yas                                   # yaşları toplamından bir yaş değişkeni oluşturduk
        return futbolcu(isim,soyisim,yas)                           # return ile futbolcu classında döndürdük

    def __lt__ (self,other):                                        # hangi futbolcunun küçük olduğunu kontrol etmek için bir fonksiyon yazdık
        if self.yas < other.yas:
            return True
        return False

futbolcu1 = futbolcu("ali","veli",23)
futbolcu2 = futbolcu("ali","atay",29)
futbolcu3 = futbolcu("ali","veli",25)

print(futbolcu1 == futbolcu2)                   # / False
print(futbolcu1 == futbolcu3)                   # / True

futbolcu4= futbolcu1 + futbolcu2
print(futbolcu4.isim)                       # / aa
print(futbolcu4.soyisim)                    # / va
print(futbolcu4.yas)                        # / 52

print(futbolcu1 > futbolcu2 )               # False 
print(futbolcu3 > futbolcu4)                # False

# # dunder methods- int

# # 1  - int.__add__()                       :    aritmatik olarak toplama
# # 2  - int.__abs__()                       : 
# # 3  - int.__and__()                       :
# # 4  - int.__bool__()                      :
# # 5  - int.__call__()                      :
# # 6  - int.__ceil__()                      :
# # 7  - int.__delattr__()                   :
# # 8  - int.__dir__()                       :
# # 9  - int.__divmod__()                    :
# # 10 - int.__eq__()                        :    eşit olup olmadığı kontrol (==)
# # 11 - int.__float__()                     :
# # 12 - int.__floor__()                     :
# # 13 - int.__floordiv__()                  :    aritmatik olarak tam bölmeye yarar.
# # 14 - int.__format__()                    :
# # 15 - int.__ge__()                        :    büyük eşit olup olmadığını kontrol (>=)
# # 16 - int.__getattribute__()              :
# # 17 - int.__getnewargs__()                :
# # 18 - int.__gt__()                        :    büyük olup olmadığını kontol (>)
# # 19 - int.__hash__()                      :
# # 20 - int.__index__()                     :
# # 21 - int.__init__()                      :
# # 22 - int.__init_subclass__()             :
# # 23 - int.__instancecheck__()             :
# # 24 - int.__int__()                       :
# # 25 - int.__invert__()                    :
# # 26 - int.__le__()                        :    küçük eşit olup olmadığını kontrol(<=)
# # 27 - int.__lshift__()                    :
# # 28 - int.__lt__()                        :    küçük olup olmadığını kontrol (<)
# # 29 - int.__mod__()                       :    aritmatik olarak mod almaya yarar.
# # 30 - int.__mul__()                       :    aritmatik olarak çarpmaya yarar
# # 31 - int.__ne__()                        :    eşit değil olup olmadığını kontrol (!=)
# # 32 - int.__neg__()                       :
# # 33 - int.__new__()                       :
# # 34 - int.__or__()                        :
# # 35 - int.__pos__()                       :
# # 36 - int.__prepare__()                   :
# # 37 - int.__pow__()                       :
# # 38 - int.__repr__()                      :
# # 39 - int.__rxor__()                      :
# # 40 - int.__radd__()                      :
# # 41 - int.__rand__()                      :
# # 42 - int.__rdivmod__()                   :
# # 43 - int.__reduce__()                    :
# # 44 - int.__reduce_ex__()                 :
# # 45 - int.__rfloordiv__()                 :
# # 46 - int.__rlshift__()                   :
# # 47 - int.__rmod__()                      :
# # 48 - int.__rmul__()                      :
# # 49 - int.__ror__()                       :
# # 50 - int.__rpow__()                      :
# # 51 - int.__rshift__()                    :
# # 52 - int.__rsub__()                      :
# # 53 - int.__repr__()                      :
# # 54 - int.__rtruediv__()                  :
# # 55 - int.__round__()                     :
# # 56 - int.__setattr__()                   :
# # 57 - int.__sizeof__()                    :
# # 58 - int.__str__()                       :
# # 59 - int.__sub__()                       :    aritmatik olarak çıkartmaya yarar.
# # 60 - int.__subclasscheck__()             :
# # 61 - int.__subclasses__()                :
# # 62 - int.__subclasshook__()              :
# # 63 - int.__truediv__()                   :
# # 64 - int.__trunc__()                     :
# # 65 - int.__xor__()                       :    aritmatik olarak üslü yazmaya yarar.

# # magic method - string

# # 1  - str.__add__()                       :    string ifadeleri uç uca ekleme
# # 2  - str.__call__()                      :
# # 3  - str.__contains__()                  :
# # 4  - str.__delattr__()                   :
# # 5  - str.__dir__()                       :
# # 6  - str.__eq__()                        :
# # 7  - str.__format__()                    :
# # 8  - str.__ge__()                        :
# # 9  - str.__getattribute__()              :
# # 10 - str.__getitem__()                   :
# # 11 - str.__getnewargs__()                :
# # 12 - str.__gt__()                        :
# # 13 - str.__hash__()                      :
# # 14 - str.__init__()                      :
# # 15 - str.__init_subclass__()             :
# # 16 - str.__instancecheck__()             :
# # 17 - str.__iter__()                      :
# # 18 - str.__le__()                        :
# # 19 - str.__len__()                       :
# # 20 - str.__lt__()                        :    
# # 21 - str.__mod__()                       :
# # 22 - str.__mul__()                       :    string ifadeyi girilen sayı kadar yan yana çarpar   
# # 23 - str.__ne__()                        :
# # 24 - str.__new__()                       :
# # 25 - str.__prepare__()                   :
# # 26 - str.__repr__()                      :
# # 27 - str.__repr__()                      :
# # 28 - str.__reduce__()                    :
# # 29 - str.__reduce_ex__()                 :
# # 30 - str.__reversed__()                  :
# # 31 - str.__rmul__()                      :
# # 32 - str.__setattr__()                   :
# # 33 - str.__sizeof__()                    :
# # 34 - str.__str__()                       :
# # 35- str.__subclasscheck__()              :
# # 36 - str.__subclasses__()                :

# # magic method - list

# # 1  - list.__add__()                      : listeleri bir liste halinde uç uca ekledi
# # 2  - list.__call__()                     :
# # 3  - list.__class_getitem__()            :
# # 4  - list.__contains__()                 :
# # 5  - list.__delattr__()                  :
# # 6  - list.__delitem__()                  :
# # 7  - list.__dir__()                      :
# # 8  - list.__eq__()                       :
# # 9  - list.__format__()                   :
# # 10 - list.__ge__()                       :
# # 11 - list.__getattribute__()             :
# # 12 - list.__getitem__()                  :
# # 13 - list.__gt__()                       :
# # 14 - list.__iadd__()                     :
# # 15 - list.__imul__()                     :
# # 16 - list.__init__()                     :
# # 17 - list.__init_subclass__()            :
# # 18 - list.__instancecheck__()            :
# # 19 - list.__iter__()                     :
# # 20 - list.__le__()                       :
# # 21 - list.__len__()                      :
# # 22 - list.__lt__()                       :
# # 23 - list.__mul__()                      :    listedeki indexleri aynı liste içerisinde girilen sayı kadar çoğaltır.
# # 24 - list.__ne__()                       :
# # 25 - list.__new__()                      :
# # 26 - list.__prepare__()                  :
# # 27 - list.__repr__()                     :
# # 28 - list.__reduce__()                   :
# # 29 - list.__reduce_ex__()                :
# # 30 - list.__reversed__()                 :
# # 31 - list.__rmul__()                     :
# # 32 - list.__setattr__()                  :
# # 33 - list.__setitem__()                  :
# # 34 - list.__sizeof__()                   :
# # 35 - list.__str__()                      :
# # 36 - list.__subclasscheck__()            :
# # 37 - list.__subclasses__()               :
# # 38 - list.__subclasshook__()             :