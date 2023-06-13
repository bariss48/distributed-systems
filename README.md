# Distributed-Systems
This repository contains distributed systems topics.

### Paralel Eleman Arama (mpi-search.py)

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

