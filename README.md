# distributed-systems
This repository contains distributed systems topics.

## Span-MDS (Minimum Dominating Set) Algoritması

Span-MDS algoritması, bir grafın minimum kümesini bulmak için kullanılan bir paralel algoritmadır. Minimum küme, bir grafın tüm düğümlerini kontrol eden en küçük düğüm kümesidir.

Algoritma, `mpi4py` kütüphanesini kullanarak paralel olarak çalışır. İşlemi MPI (Message Passing Interface) ile dağıtarak, her işlemci kendi parçasında belirli bir aralığı kontrol eder ve sonuçları birleştirir.

Algoritmanın ana adımları şu şekildedir:

1. MPI başlatılır ve işlemci sayısı ve sıralama bilgileri alınır.
2. Veri listesi, işlemci sayısına göre eşit parçalara bölünür. Her işlemciye bir parça atanır.
3. Her işlemci, kendi parçasındaki veri üzerinde hedef elemanı arar.
4. Her işlemcinin sonucu toplanır ve birleştirilir.
5. Sıralama 0 olan işlemci, birleştirilmiş sonuçları değerlendirir ve hedef elemanın bulunup bulunmadığını belirler.
6. MPI sonlandırılır.

Bu algoritma, paralel hesaplama gücünden faydalanarak graf üzerinde etkili bir çözüm sunar. İşlemci sayısının artmasıyla hesaplama süresi hızlanır ve büyük graf yapıları üzerinde verimli bir şekilde çalışır.
