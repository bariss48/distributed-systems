from random import randint

class Node:
    def __init__(self, id):
        self.id = id
        self.komsular = []       # Düğümün komşularını saklamak için bir liste
        self.ziyaret_edildi = False    # Düğümün ziyaret edilip edilmediğini tutmak için bir bayrak

    def komsu_ekle(self, komsu):
        self.komsular.append(komsu)     # Düğüme bir komşu eklemek için kullanılan fonksiyon

def tarry_mst(nodes):
    baslangic_dugumu = nodes[randint(0, len(nodes) - 1)]   # Rastgele bir başlangıç düğümü seçilir
    baslangic_dugumu.ziyaret_edildi = True    # Başlangıç düğümü ziyaret edildi olarak işaretlenir

    iletisim_kuyrugu = [baslangic_dugumu]    # İletişim kuyruğu için bir liste oluşturulur ve başlangıç düğümü ile başlatılır

    while iletisim_kuyrugu:    # İletişim kuyruğu boş olana kadar aşağıdaki adımlar tekrarlanır
        gonderen_dugum = iletisim_kuyrugu.pop(0)   # Kuyruğun başından bir gönderen düğüm alınır
        for komsu in gonderen_dugum.komsular:   # Gönderen düğümün komşuları üzerinde döngü yapılır
            if not komsu.ziyaret_edildi:   # Komşu düğüm ziyaret edilmemişse
                print(f"{gonderen_dugum.id} -> {komsu.id}")   # Gönderen düğümün komşusuna bir ileti gönderildiğini belirtmek için çıktı verilir
                komsu.ziyaret_edildi = True   # Komşu düğüm ziyaret edildi olarak işaretlenir
                iletisim_kuyrugu.append(komsu)   # Komşu düğüm iletişim kuyruğuna eklenir

        if iletisim_kuyrugu:   # İletişim kuyruğu hala boş değilse
            son_dugum = iletisim_kuyrugu[-1]   # Kuyruğun sonundaki düğüm alınır
            if son_dugum != baslangic_dugumu:
                print(f"{son_dugum.id} -> {baslangic_dugumu.id}")   # Son düğümün başlangıç düğümüne bir ileti gönderdiği belirtilir
                iletisim_kuyrugu.append(baslangic_dugumu)   # Başlangıç düğümü iletişim kuyruğuna eklenir

if __name__ == '__main__':
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node0.komsu_ekle(node1)   # Düğümler arasında bağlantılar tanımlanır
    node0.komsu_ekle(node3)
    node1.komsu_ekle(node0)
    node1.komsu_ekle(node2)
    node1.komsu_ekle(node4)
    node2.komsu_ekle(node1)
    node2.komsu_ekle(node3)
    node3.komsu_ekle(node0)
    node3.komsu_ekle(node2)
    node3.komsu_ekle(node4)
    node4.komsu_ekle(node1)
    node4.komsu_ekle(node3)

    tarry_mst([node0, node1, node2, node3, node4])   # Tarry'nin token tabanlı MST algoritmasını çağırarak çalıştırır
