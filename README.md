# Distributed-Systems
This repository contains distributed systems topics.

## Paralel Eleman Arama (mpi-search.py)

Bu Python kod örneği, verilen bir veri listesinde belirli bir hedef elemanın var olup olmadığını paralel olarak arayan basit bir MPI (Message Passing Interface) uygulamasını göstermektedir.

Kodun çalışma mantığı şu adımları izler:

1. İlk olarak, `eleman_ara` fonksiyonu tanımlanır ve veri listesi ile hedef eleman parametre olarak alınır.

2. MPI başlatılır ve her işlemciye sırasıyla `rank` ve `size` değerleri atanır. `rank`, her işlemcinin benzersiz bir kimliğini temsil ederken, `size` ise toplam işlemci sayısını ifade eder.

3. Veri listesi, toplam işlemci sayısına göre eşit parçalara bölünür. Her işlemciye bir parça atanır. Son işlemciye ek parçalar atanırken, diğer işlemcilerin parça boyutu aynı olacak şekilde dikkate alınır.

4. Her işlemci kendi parçasında hedef elemanı arar. Parça sınırları, `baslangic` ve `bitis` değişkenleri kullanılarak belirlenir.

5. Her işlemcinin kendi parçasında döngü kullanarak hedef elemanı araması gerçekleştirilir. Eğer hedef eleman bulunursa, `True` değeri döndürülür.

6. Sonuçlar, `comm.gather()` fonksiyonu kullanılarak birleştirilir. Toplama işlemi, 0 numaralı işlemci tarafından gerçekleştirilir.

7. Sonuçların işlenmesi, 0 numaralı işlemci tarafından yapılır. `any()` fonksiyonu kullanılarak toplanan sonuçlardan herhangi biri `True` ise hedef elemanın bulunduğu belirtilir, aksi takdirde bulunamadığı ifade edilir.

8. MPI sonlandırılır ve program sonlanır.

Bu kod, paralel hesaplama yeteneklerini kullanarak veri üzerinde arama işlemini hızlandırmaktadır. Her işlemcinin kendi parçasında bağımsız olarak çalışması, veri listesinin parçalara bölünerek paralel olarak işlenmesini sağlar. Böylece, performans artışı elde edilir ve büyük veri kümesi üzerinde arama işlemi daha etkili bir şekilde gerçekleştirilir.

## Span MDS (span-mds.py)

### install dependencies
```
$ pip install matplotlib

$ pip install scikit-learn 

$ pip install scipy
```
### run
```
$ python3.11 span-mds.py 
```

Spanning MDS (Minimum Spanning Tree Multidimensional Scaling), bir veri kümesini düşük boyutlu bir uzayda temsil etmek için kullanılan bir algoritmadır. Algoritma, veri noktaları arasındaki mesafeleri hesaplar, ardından bu mesafeleri kullanarak minimum ağacı bulur ve son olarak çok boyutlu ölçeklendirmeyi (MDS) uygular.

### Algoritma Adımları

1. Veri kümesinin noktalarının koordinatları belirlenir.
2. Noktalar arasındaki mesafeler hesaplanır. Öklidyen mesafe, genellikle bu hesaplama için kullanılan bir metriktir.
3. Minimum ağacın oluşturulması için veri noktaları arasındaki mesafeler kullanılır. Minimum ağaç, veri noktalarını birleştiren en kısa mesafeli kenarları içerir.
4. MDS (Çok Boyutlu Ölçekleme) uygulanır. MDS, veri noktalarını düşük boyutlu bir uzaya projeksiyon yaparak, orijinal veri yapısını korur.
5. Sonuç olarak, veri noktaları düşük boyutlu bir uzayda temsil edilir.

### Örnek çıktı

![Figure_1](https://github.com/bariss48/distributed-systems/assets/50153950/02d7d4d0-85e7-4d50-9b75-21436c694bfe)


## Terry-Token Algoritması (terry-token.py)

Terry-Token Algoritması, iletişim ağlarındaki düğümler arasında eşit miktarda veri transferi sağlamak için kullanılan bir algoritmadır. Bu algoritma, dağıtılmış sistemlerde kullanılan token tabanlı bir protokoldür.

### Algoritma Adımları

1. İletişim ağındaki düğümler bir halka şeklinde düzenlenir. Her düğüm, veri paketlerini almak ve göndermek için bir token'e sahiptir.
2. Algoritma başladığında, bir başlatma düğümü token'i alır ve veri transferini başlatır.
3. Başlatma düğümü, token'i alarak bir veri paketini hedef düğüme gönderir.
4. Hedef düğüm, veri paketini alır ve gerektiğinde işler. Daha sonra, veri paketini bir sonraki hedef düğüme yönlendirir.
5. Token, son hedef düğüme ulaştığında, son düğüm veri paketini işledikten sonra token'i bir sonraki düğüme ileterek veri transferini sürdürür.
6. Bu süreç, token halkasının tüm düğümlerini dolaşana kadar devam eder. Her düğüm, token'i alarak veri paketlerini işler ve bir sonraki düğüme ileterek döngüyü sürdürür.
7. Token halkası tam bir döngü yaptığında, veri transferi tamamlanır.

Terry-Token Algoritması, iletişim ağlarında veri transferinin düzenlenmesini sağlar ve eşit miktarda veri transferini her düğüm üzerinde gerçekleştirir.

### Örnek çıktı
![Ekran Resmi 2023-06-13 22 09 25](https://github.com/bariss48/distributed-systems/assets/50153950/cddc5930-23d9-4775-857f-db8c53d2e1ec)





