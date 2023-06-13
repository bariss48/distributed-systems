from mpi4py import MPI

def eleman_ara(veri_listesi, hedef_eleman):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Veri listesinin eşit parçalara bölünmesi
    parca_boyutu = len(veri_listesi) // size
    baslangic = rank * parca_boyutu
    bitis = baslangic + parca_boyutu

    # Son process için ek parçalar
    if rank == size - 1:
        bitis = len(veri_listesi)

    # Her processin kendi parçasında hedef elemanı araması
    for i in range(baslangic, bitis):
        if veri_listesi[i] == hedef_eleman:
            return True

    return False

if __name__ == '__main__':
    veri_listesi = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    hedef = 12

    # MPI başlatma
    MPI.Init()

    # Her processin hedef elemanı araması
    sonuc = eleman_ara(veri_listesi, hedef)

    # Sonuçların toplanması
    tum_sonuclar = comm.gather(sonuc, root=0)

    # Sonuçların işlenmesi
    if rank == 0:
        if any(tum_sonuclar):
            print("Hedef eleman bulundu.")
        else:
            print("Hedef eleman bulunamadı.")

    # MPI sonlandırma
    MPI.Finalize()