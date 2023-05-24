# dunder methods (magic methods)

# what is the dunder methods : 

# Python'da özel davranışlar tanımlamak için kullanılır ve bir nesnenin bazı temel işlemlerini özelleştirmek veya üzerinde çalışmak istediğimiz durumlarda kullanılır. 
# Bu metotlar, bir sınıfın içinde tanımlanır ve sınıfın özel davranışlarını kontrol etmemizi sağlar.

# python üzerinde daha önceden tanımlı ve görevi olan fonksiyonlardır. 
# __ ile başlayıp bitiyor olması onları tanımamıza yarar. double underscore kısaltmasıdır.

print(int.__add__(3,5))
print( 3 + 5 )               # / 8

# bizim yazdığımız : print( 3 + 5 )  pythonun anladığı print(int.__add__(3,5))

print("ali"+" " + "veli")          # / ali veli
# bizim yazdığımız : print("ali"+"veli")  pythonun anladığı print(str.__add__(ali,veli))

print([1,2,3] + [4,5,6])     # / [1,2,3,4,5,6]

# bizim yazdığımız : print([1,2,3] + [4,5,6])  pythonun anladığı print(list.__add__([1,2,3],[4,5,6]))

print(int.__mul__(8,2))             # 8 ile 2 yi aritmatik olarak çarpar.
print(str.__mul__("Oğuz",7))        # oğuz ile 7 yi string olarak çarçar( string olarak çarpmak demek uç uca eklemek demektir.)
print(list.__mul__([1,2,3],3))      # [1,2,3] dizisini 3 ile liste olarak çarpar ( liste olarak çarpmak demek uç uca eklemek demektir.)
print(int.__sub__(6,4))             # 6 dan 4ü aritmatik olarak çıkarmak.

class Mylist(list):             # list klasından miras alarak yeni bir class oluşturduk.
    pass                        # pass geçtiğim için miras olarak aldığım list clasına ait bütün özellikler birebir kullanılacak.

liste1 = Mylist([1,2,3])
liste2 = Mylist([4,5,6])

print(liste1 + liste2)          # / [1, 2, 3, 4, 5, 6]  listelerdeki standart dunder metot olarak list.__add__() çalıştı.

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

# dunder methods- int

# 1  - int.__add__()                                    :    aritmatik olarak toplama
# 2  - int.__abs__()                                    :    Mutlak değeri döndürmek için kullanılan bir metod
# 3  - int.__and__()                                    :    Bit düzeyinde "ve" işlemini gerçekleştirmek için kullanılan bir metod. 
# 4  - int.__bool__()                                   :    Nesnenin True veya False olarak değerlendirilmesi için kullanılan bir metod
# 5  - int.__call__()                                   :    Nesnenin çağrılabilir bir işlev gibi davranmasını sağlayan bir metod. 
# 6  - int.__ceil__()                                   :    Yerleşik math.ceil() işlevi gibi davranarak int değerinin yukarı yuvarlanmış bir tamsayı değerini döndüren bir metod.
# 7  - int.__delattr__()                                :    Nesnenin bir özelliğini silmek için kullanılan bir metod.
# 8  - int.__dir__()                                    :    Nesnenin sahip olduğu özniteliklerin listesini döndüren bir metod.
# 9  - int.__divmod__()                                 :    Bölme işlemi sonucunda kalan ve bölümü birlikte döndüren bir metod
# 10 - int.__eq__()                                     :    eşit olup olmadığı kontrol (==)
# 11 - int.__float__()                                  :    Bir int değerini ondalık bir kayan nokta sayısına dönüştürmek için kullanılan bir metod.
# 12 - int.__floor__()                                  :    Yerleşik math.floor() işlevi gibi davranarak int değerinin aşağı yuvarlanmış bir tamsayı değerini döndüren bir metod.
# 13 - int.__floordiv__()                               :    İki int değeri arasında tam bölme işlemini gerçekleştirmek için kullanılan bir metod. // operatörü ile kullanıldığında bu metod çağrılır.
# 14 - int.__format__()                                 :    Nesnenin belirli bir biçimlendirme stilinde bir dizeye dönüştürülmesi için kullanılan bir metod.
# 15 - int.__ge__()                                     :    Büyük eşit (>=) karşılaştırma operatörünü gerçekleştiren bir metod.
# 16 - int.__getattribute__()                           :    Nesnenin belirtilen bir özniteliğine erişmek için kullanılan bir metod.
# 17 - int.__getnewargs__()                             :    int nesnesinin pickle tarafından nasıl yeniden oluşturulabileceğini temsil eden bir metod.
# 18 - int.__gt__()                                     :    Büyük (>) karşılaştırma operatörünü gerçekleştiren bir metod.
# 19 - int.__hash__()                                   :    Nesnenin karma değerini hesaplamak için kullanılan bir metod.
# 20 - int.__index__()                                  :    Bir int değerini tamsayı indeks olarak kullanmak için kullanılan bir metod.
# 21 - int.__init__()                                   :    int nesnesinin başlatılması için kullanılan bir metod
# 22 - int.__init_subclass__()                          :    int sınıfının alt sınıflarının başlatılması için kullanılan bir metod.
# 23 - int.__instancecheck__()                          :    Bir nesnenin bir int türüne ait olup olmadığını kontrol etmek için kullanılan bir metod.
# 24 - int.__int__()                                    :    Bir int nesnesini int türüne dönüştürmek için kullanılan bir metod.
# 25 - int.__invert__()                                 :    Ters çevirme (bit flip) işlemi için kullanılan bir metod. ~ operatörü ile kullanıldığında bu metod çağrılır.
# 26 - int.__le__()                                     :    Küçük eşit (<=) karşılaştırma operatörünü gerçekleştiren bir metod.
# 27 - int.__lshift__()                                 :    Bit düzeyinde sola kaydırma işlemi için kullanılan bir metod. << operatörü ile kullanıldığında bu metod çağrılır.
# 28 - int.__lt__()                                     :    küçük olup olmadığını kontrol (<)
# 29 - int.__mod__()                                    :    aritmatik olarak mod almaya yarar.
# 30 - int.__mul__()                                    :    aritmatik olarak çarpmaya yarar
# 31 - int.__ne__()                                     :    eşit değil olup olmadığını kontrol (!=)
# 32 - int.__neg__()                                    :    Negatif değeri döndürmek için kullanılan bir metod. - operatörü ile kullanıldığında bu metod çağrılır.
# 33 - int.__new__()                                    :    Yeni bir int nesnesi oluşturmak için kullanılan bir metod.
# 34 - int.__or__()                                     :    Bit düzeyinde "veya" işlemini gerçekleştirmek için kullanılan bir metod. | operatörü ile kullanıldığında bu metod çağrılır.
# 35 - int.__pos__()                                    :    Pozitif değeri döndürmek için kullanılan bir metod. + operatörü ile kullanıldığında bu metod çağrılır.
# 36 - int.__prepare__()                                :    Yöntem çözümlemesi sırasında kullanılan bir metod.
# 37 - int.__pow__()                                    :    Üs alma (**) işlemi için kullanılan bir metod.
# 38 - int.__repr__()                                   :    Nesnenin gösterimini (repr()) döndüren bir metod.
# 39 - int.__rxor__()                                   :    Sağdan "veya ötelemeli veya" işlemini gerçekleştiren bir metod. ^ operatörü ile kullanıldığında bu metod çağrılır.
# 40 - int.__radd__()                                   :    Sağdan toplama (+) işlemini gerçekleştiren bir metod.
# 41 - int.__rand__()                                   :    Sağdan "ve" işlemini gerçekleştiren bir metod.
# 42 - int.__rdivmod__()                                :    Sağdan bölme ve mod alma işlemini gerçekleştiren bir metod.
# 43 - int.__reduce__()                                 :    Nesneyi yeniden oluşturmak için kullanılan bir metod.
# 44 - int.__reduce_ex__()                              :    Nesneyi yeniden oluşturmak için kullanılan bir metod.
# 45 - int.__rfloordiv__()                              :    Sağdan tam bölmeyi gerçekleştiren bir metod.
# 46 - int.__rlshift__()                                :    Sağdan sola kaydırmayı gerçekleştiren bir metod.
# 47 - int.__rmod__()                                   :    Sağdan mod alma işlemini gerçekleştiren bir metod.
# 48 - int.__rmul__()                                   :    Sağdan çarpma işlemini gerçekleştiren bir metod. 
# 49 - int.__ror__()                                    :    Sağdan "veya" işlemini gerçekleştiren bir metod.
# 50 - int.__rpow__()                                   :    Sağdan üs alma işlemini gerçekleştiren bir metod.
# 51 - int.__rshift__()                                 :    Sağdan bit düzeyinde sağa kaydırma işlemini gerçekleştiren bir metod.
# 52 - int.__rsub__()                                   :    Sağdan çıkarma işlemini gerçekleştiren bir metod.
# 53 - int.__repr__()                                   :    Nesnenin gösterimini (repr()) döndüren bir metod.
# 54 - int.__rtruediv__()                               :    Sağdan gerçek bölmeyi gerçekleştiren bir metod.
# 55 - int.__round__()                                  :    Yuvarlama işlemi için kullanılan bir metod.
# 56 - int.__setattr__()                                :    Nesnenin bir özniteliğini ayarlamak için kullanılan bir metod.
# 57 - int.__sizeof__()                                 :    Nesnenin bellekte kapladığı yerin boyutunu döndüren bir metod.
# 58 - int.__str__()                                    :    Nesnenin dize temsili (str()) döndüren bir metod.
# 59 - int.__sub__()                                    :    Çıkarma (-) işlemini gerçekleştiren bir metod.
# 60 - int.__subclasscheck__()                          :    Bir sınıfın bir alt sınıfı olup olmadığını kontrol etmek için kullanılan bir metod.
# 61 - int.__subclasses__()                             :    Bir sınıfın alt sınıflarının listesini döndüren bir metod.
# 62 - int.__subclasshook__()                           :    Bir alt sınıfın belirli bir sınıfı temsil ettiğini kontrol etmek için kullanılan bir metod.
# 63 - int.__truediv__()                                :    Gerçek bölme (/) işlemini gerçekleştiren bir metod.
# 64 - int.__trunc__()                                  :    Tamsayı kısmını döndüren bir metod.
# 65 - int.__xor__()                                    :    Bit düzeyinde "veya ötelemeli veya" işlemini gerçekleştiren bir metod. ^ operatörü ile kullanıldığında bu metod çağrılır.


# magic method - string
# 1  - str.__add__()                                    :   İki string ifadeyi birleştirmek için kullanılan bir metod. + operatörü ile kullanıldığında bu metod çağrılır.
# 2  - str.__call__()                                   :   Bir nesnenin çağrılabilir bir işlev gibi davranmasını sağlamak için kullanılan bir metod.
# 3  - str.__contains__()                               :   Bir string ifadenin başka bir string ifade içinde bulunup bulunmadığını kontrol etmek için kullanılan bir metod. in operatörü ile kullanıldığında bu metod çağrılır.
# 4  - str.__delattr__()                                :   Bir nesnenin bir özelliğini silmek için kullanılan bir metod.
# 5  - str.__dir__()                                    :   Bir nesnenin geçerli etiketlerini döndüren bir metod.
# 6  - str.__eq__()                                     :   İki string ifadenin eşit olup olmadığını kontrol etmek için kullanılan bir metod. == operatörü ile kullanıldığında bu metod çağrılır.
# 7  - str.__format__()                                 :   Bir string ifadeyi belirli bir biçime dönüştürmek için kullanılan bir metod.
# 8  - str.__ge__()                                     :   Büyük eşit (>=) karşılaştırma operatörünü gerçekleştiren bir metod.
# 9  - str.__getattribute__()                           :   Bir nesnenin bir özniteliğine erişmek için kullanılan bir metod.
# 10 - str.__getitem__()                                :   Bir string ifadenin belirli bir indeksteki karakterini döndüren bir metod. [] operatörü ile kullanıldığında bu metod çağrılır.
# 11 - str.__getnewargs__()                             :   Nesneyi yeniden oluşturmak için kullanılan bir metod.
# 12 - str.__gt__()                                     :   Büyük (>) karşılaştırma operatörünü gerçekleştiren bir metod.
# 13 - str.__hash__()                                   :   Nesnenin karma değerini döndüren bir metod.
# 14 - str.__init__()                                   :   Bir string nesnesinin başlatılması için kullanılan bir metod.
# 15 - str.__init_subclass__()                          :   str sınıfının alt sınıflarının başlatılması için kullanılan bir metod.
# 16 - str.__instancecheck__()                          :   Bir nesnenin bir str türüne ait olup olmadığını kontrol etmek için kullanılan bir metod.
# 17 - str.__iter__()                                   :   Bir string ifade üzerinde yinelemeyi (iterasyon) sağlayan bir metod.
# 18 - str.__le__()                                     :   Küçük eşit (<=) karşılaştırma operatörünü gerçekleştiren bir metod.
# 19 - str.__len__()                                    :   Bir string ifadenin uzunluğunu döndüren bir metod.
# 20 - str.__lt__()                                     :   Küçük (<) karşılaştırma operatörünü gerçekleştiren bir metod.
# 21 - str.__mod__()                                    :   Biçimlendirme işlemi için kullanılan bir metod.
# 22 - str.__mul__()                                    :   Bir string ifadeyi belirli bir sayıkadar çoğaltmak için kullanılan bir metod. * operatörü ile kullanıldığında bu metod çağrılır.
# 23 - str.__ne__()                                     :   Eşit olmayan (!=) karşılaştırma operatörünü gerçekleştiren bir metod.
# 24 - str.__new__()                                    :   Yeni bir str nesnesi oluşturmak için kullanılan bir metod.
# 25 - str.__prepare__()                                :   Yöntem çözümlemesi sırasında kullanılan bir metod.
# 26 - str.__repr__()                                   :   Nesnenin gösterimini (repr()) döndüren bir metod.
# 27 - str.__reduce__()                                 :   Nesneyi yeniden oluşturmak için kullanılan bir metod.
# 28 - str.__reduce_ex__()                              :   Nesneyi yeniden oluşturmak için kullanılan bir metod.
# 29 - str.__reversed__()                               :   Bir string ifadenin tersini döndüren bir metod.
# 30 - str.__rmul__()                                   :   Sağdan çarpma işlemini gerçekleştiren bir metod.
# 31 - str.__setattr__()                                :   Bir nesnenin bir özniteliğini ayarlamak için kullanılan bir metod.
# 32 - str.__sizeof__()                                 :   Nesnenin bellekte kapladığı yerin boyutunu döndüren bir metod.
# 33 - str.__str__()                                    :   Nesnenin dize temsili (str()) döndüren bir metod.
# 34 - str.__subclasscheck__()                          :   Bir sınıfın bir alt sınıfı olup olmadığını kontrol etmek için kullanılan bir metod.
# 35 - str.__subclasses__()                             :   Bir sınıfın alt sınıflarının listesini döndüren bir metod.

# magic method - list

# 1  - list.__add__(self, other)                        :   İki listeyi birleştirmek için kullanılır. İlk listenin sonuna ikinci listenin elemanlarını ekler ve yeni bir listeyi döndürür.
# 2  - list.__call__(self, *args, **kwargs)             :   Bir liste nesnesi çağrıldığında çalışır. Bu yöntemi kullanmak, listenin çağrıldığında gerçekleştirilecek özel bir davranış tanımlamak için kullanılabilir.
# 3  - list.__class_getitem__(cls, item)                :   Sınıfın içindeki öğeleri almak için kullanılır. Örneğin, list[int] ifadesi, listenin içindeki tamsayıları ifade eder.
# 4  - list.__contains__(self, item)                    :   Bir listenin belirli bir öğeyi içerip içermediğini kontrol etmek için kullanılır. Eğer öğe listede varsa True, yoksa False döndürür.
# 5  - list.__delattr__(self, name)                     :   Bir listenin belirli bir özniteliğini silmek için kullanılır. Öznitelik adı name olarak belirtilir.
# 6  - list.__delitem__(self, index)                    :   Bir listenin belirli bir indeksine sahip öğeyi silmek için kullanılır.
# 7  - list.__dir__(self)                               :   Bir listenin sahip olduğu öznitelikleri listeler. Bu yöntem, listenin kullanılabilir özel yöntemlerini ve özniteliklerini döndürür.
# 8  - list.__eq__(self, other)                         :   İki listenin eşit olup olmadığını kontrol etmek için kullanılır. Eğer listeler aynı öğeleri aynı sırayla içeriyorsa True, aksi halde False döndürür.
# 9  - list.__format__(self, format_spec)               :   Bir listenin biçimlendirilmiş bir dize temsilini döndürmek için kullanılır. format_spec parametresi, biçimlendirme işlemini kontrol eden bir biçimlendirme dizesini belirtir.
# 10 - list.__ge__(self, other)                         :   Bir listenin diğer bir listeden daha büyük veya eşit olduğunu kontrol etmek için kullanılır.
# 11 - list.__getattribute__(self, name)                :   Bir listenin belirli bir özniteliğini almak için kullanılır.
# 12 - list.__getitem__(self, index)                    :   Bir listenin belirli bir indeksine sahip öğeyi almak için kullanılır.
# 13 - list.__gt__(self, other)                         :   Bir listenin diğer bir listeden daha büyük olduğunu kontrol etmek için kullanılır.
# 14 - list.__iadd__(self, other)                       :   İkinci bir listeyi ilk listenin sonuna ekleyerek ilk listeyi değiştirir.
# 15 - list.__imul__(self, other)                       :   Bir listenin kendisini bir sayıyla çarparak kendisini değiştirir.
# 16 - list.__init__(self, *args, **kwargs)             :   Bir liste nesnesi oluşturulduğunda çalışır. Bu yöntem, listenin başlangıç durumunu ayarlamak için kullanılır.
# 17 - list.__init_subclass__(...)                      :   Alt sınıflar oluşturulduğunda çağrılan bir metottur. Liste sınıfının alt sınıflarını özelleştirmek için kullanılabilir.
# 18 - list.__instancecheck__(self, instance)           :   Bir nesnenin bir listenin örneği olup olmadığını kontrol etmek için kullanılır.
# 19 - list.__iter__(self)                              :   Bir listenin üzerinde döngü oluşturmak için kullanılır. Listenin elemanlarını birer birer döndüren bir yineleyici (iterator) döndürür.
# 20 - list.__le__(self, other)                         :   Bir listenin diğer bir listeden daha küçük veya eşit olduğunu kontrol etmek için kullanılır.
# 21 - list.__len__(self)                               :   Bir listenin eleman sayısını döndürmek için kullanılır.
# 22 - list.__lt__(self, other)                         :   Bir listenin diğer bir listeden daha küçük olduğunu kontrol etmek için kullanılır.
# 23 - list.__mul__(self, other)                        :   Bir listenin kendisini belirli bir sayıyla çoğaltarak yeni bir listeyi döndürür.
# 24 - list.__ne__(self, other)                         :   İki listenin eşit olup olmadığını kontrol etmek için kullanılır. Eğer listeler aynı öğeleri aynı sırayla içermiyorsa True, aksi halde False döndürür.
# 25 - list.__new__(cls, *args, **kwargs)               :   Bir liste nesnesi oluşturulduğunda çağrılan bir metottur. Bu yöntem, yeni bir liste nesnesi oluşturmak için kullanılır.
# 26 - list.__prepare__(...)                            :   Alt sınıflar oluşturulduğunda çağrılan bir metottur. Liste sınıfının alt sınıflarının hazırlanmasını sağlamak için kullanılabilir.
# 27 - list.__repr__(self)                              :   Bir listenin temsilini döndürmek için kullanılır. Bu yöntem, listenin bir dize temsilini oluşturur.
# 28 - list.__reduce__(self)                            :   Bir listenin serileştirilmesi için kullanılır.
# 29 - list.__reduce_ex__(self, protocol)               :   Bir listenin serileştirilmesi için kullanılır. Daha eski protokollerle uyumlu bir serileştirme sağlamak için kullanılabilir.
# 30 - list.__reversed__(self)                          :   Bir listenin tersine çevrilmiş bir kopyasını döndürür.
# 31 - list.__rmul__(self, other)                       :   Bir listenin kendisini belirli bir sayıyla çoğaltarak yeni bir listeyi döndürür.
# 32 - list.__setattr__(self, name, value)              :   Bir listenin belirli bir özniteliğini ayarlamak için kullanılır.
# 33 - list.__setitem__(self, index, value)             :   Bir listenin belirli bir indeksine sahip öğeyi değiştirmek için kullanılır.
# 34 - list.__sizeof__(self)                            :   Bir listenin bellekte kapladığı boyutu döndürür.
# 35 - list.__str__(self)                               :   Bir listenin dize temsilini döndürür.
# 36 - list.__subclasscheck__(cls, subclass)            :   Bir alt sınıfın bir listenin alt sınıfı olup olmadığını kontrol etmek için kullanılır
# 37 - list.__subclasses__(cls)                         :   Bir listenin alt sınıflarını döndürür.
# 38 - list.__subclasshook__(cls, subclass)             :   Bir alt sınıfın bir listenin alt sınıfı olup olmadığını kontrol etmek için kullanılır. Bu yöntem, alt sınıfların kontrol edilmesi için kullanılan bir kancadır.
