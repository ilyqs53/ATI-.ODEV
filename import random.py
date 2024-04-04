import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Verilen sabit değerler
# Bu komut parçacığında sırasıyla 30 derecenin radiant karşılığını, yer çekimini ve  topun konumunu(x=0,y=okul numarasının son 2 hanesi) koda bildirdim.
aci = math.radians(30)  
g = 9.81  
top_konum = [0, 11]  
kalan_yükseklik_sabiti=0.0458965874
kalan_yükseklik_sabiti2=0.0478651648
# Yukardaki iki değer sabittir ve ortalamadır bunlar noktanın kesin olmamasındandır.
# Bu değerlerin olma sebebi şudur top verilen okul numaraları kadar yüksektedir.
# verdiğim tabloda - ye düşürerek bu farkı kapattım. 
# Hedefin konumu  
# Hedefin toptan uzaklığını istenilen üzere % 20 random payıyla ayarladım. 
uzaklik_mesafesi = 20000 + 200 * random.randint(-10, 10)
genislik_baslangic = uzaklik_mesafesi
genislik_bitis = uzaklik_mesafesi + 1000 + 100 * random.randint(-2, 2)
if uzaklik_mesafesi<20000:
  def atis_simulasyonu(hiz_alt_siniri, hiz_ust_siniri):
    atis_sayisi = 0
    while True:
        atis_sayisi += 1
        hiz = (hiz_alt_siniri + hiz_ust_siniri) / 2
        ucus_suresi = kalan_yükseklik_sabiti+(2 * hiz * math.sin(aci)) / g
        menzil = hiz * math.cos(aci) * ucus_suresi
        dusme_noktasi = top_konum[0] + menzil
        # Hedefe olan uzaklığı kontrol et
        if dusme_noktasi < genislik_baslangic:
            mesafe_farki = genislik_baslangic - dusme_noktasi
            print(f"Atış {atis_sayisi}: Hedefin önüne düştü.  Hız: {hiz} m/s")
            hiz_alt_siniri = hiz
        elif dusme_noktasi > genislik_bitis:
            mesafe_farki = dusme_noktasi - genislik_bitis
            print(f"Atış {atis_sayisi}: Hedefe uzağına düştü.  Hız: {hiz} m/s")
            hiz_ust_siniri = hiz
        else:
            mesafe_farki = 0
            print(f"Atış {atis_sayisi}: Hedefe tam isabetle vuruldu. Hız: {hiz} m/s")
            # İsabet eden atışın grafiğini çizme
            t = np.linspace(0, ucus_suresi, num=300)
            x = hiz * np.cos(aci) * t
            y = hiz * np.sin(aci) * t - (0.5 * g * t**2)
            plt.figure(figsize=(12, 6))
            plt.plot(x, y, 'b-', label='Atış Yolu')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(genislik_baslangic, color='k', linestyle='--', label='Hedef Başlangıcı')
            plt.axvline(genislik_bitis, color='k', linestyle='--', label='Hedef Bitişi')
            plt.title('Top Mermisi Atış Grafiği')
            plt.xlabel('Mesafe (metre)')
            plt.ylabel('Yükseklik (metre)')
            plt.legend()
            plt.grid(True)
            plt.show()
            break
else:
 def atis_simulasyonu(hiz_alt_siniri, hiz_ust_siniri):
    atis_sayisi = 0
    while True:
        atis_sayisi += 1
        hiz = (hiz_alt_siniri + hiz_ust_siniri) / 2
        ucus_suresi = kalan_yükseklik_sabiti2+(2 * hiz * math.sin(aci)) / g
        menzil = hiz * math.cos(aci) * ucus_suresi
        dusme_noktasi = top_konum[0] + menzil
        if dusme_noktasi < genislik_baslangic:
            mesafe_farki = genislik_baslangic - dusme_noktasi
            print(f"Atış {atis_sayisi}: Hedefin önüne düştü.  Hız: {hiz} m/s")
            hiz_alt_siniri = hiz
        elif dusme_noktasi > genislik_bitis:
            mesafe_farki = dusme_noktasi - genislik_bitis
            print(f"Atış {atis_sayisi}: Hedefe uzağına düştü.  Hız: {hiz} m/s")
            hiz_ust_siniri = hiz
        else:
            mesafe_farki = 0
            print(f"Atış {atis_sayisi}: Hedefe tam isabetle vuruldu. Hız: {hiz} m/s")
            t = np.linspace(0, ucus_suresi, num=300)
            x = hiz * np.cos(aci) * t
            y = hiz * np.sin(aci) * t - (0.5 * g * t**2)
            plt.figure(figsize=(12, 6))
            plt.plot(x, y, 'b-', label='Atış Yolu')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(genislik_baslangic, color='k', linestyle='--', label='Hedef Başlangıcı')
            plt.axvline(genislik_bitis, color='k', linestyle='--', label='Hedef Bitişi')
            plt.title('Top Mermisi Atış Grafiği')
            plt.xlabel('Mesafe (metre)')
            plt.ylabel('Yükseklik (metre)')
            plt.legend()
            plt.grid(True)
            plt.show()
            break

# İlk atış için hız sınırları
hiz_alt_siniri = 330  # m/s
hiz_ust_siniri = 1800  # m/s

# Atış simülasyonunu ve grafiğini çizme
atis_simulasyonu(hiz_alt_siniri, hiz_ust_siniri)