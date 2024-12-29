# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:13:10 2024

@author: nisak
"""

def kredi_notu_hesapla(gelir, ev_sayisi, araba_sayisi, arsa_sayisi, borc, calisma_yili, egitim, medeni_durum):
    # Gelir Düzeyi Puanı
    if gelir < 10000:
        gelir_puan = 500
    elif 10000 <= gelir < 20000:
        gelir_puan = 1000
    elif 20000 <= gelir < 40000:
        gelir_puan = 2000
    elif 40000 <= gelir < 60000:
        gelir_puan = 3000
    else:
        gelir_puan = 4000
    
    # Ev Sayısı Puanı
    ev_puan = min(ev_sayisi * 100, 300)  # Her ev için 100 puan, maksimum 300 puan

    # Araba Sayısı Puanı
    araba_puan = min(araba_sayisi * 60, 180)  # Her araba için 60 puan, maksimum 180 puan

    # Arsa Sayısı Puanı
    arsa_puan = min(arsa_sayisi * 80, 240)  # Her arsa için 80 puan, maksimum 240 puan

    # Borç Durumu Puanı
    if borc == 0:
        borc_puan = 2000
    elif borc < 10000:
        borc_puan = 1000
    elif 10000 <= borc < 30000:
        borc_puan = 500
    else:
        borc_puan = 50

    # Çalışma Süresi Puanı
    if calisma_yili <= 5:
        calisma_puan = 500
    elif 6 <= calisma_yili <= 10:
        calisma_puan = 1000
    elif 11 <= calisma_yili <= 20:
        calisma_puan = 2000
    else:
        calisma_puan = 3000

    # Eğitim Düzeyi Puanı
    egitim_puan = {
        "Ortaokul Mezunu": 50,
        "Lise Mezunu": 100,
        "Üniversite": 150,
        "Yüksek Lisans": 200,
        "Doktora": 250
    }.get(egitim, 0)

    # Medeni Durum Puanı
    medeni_puan = 100 if medeni_durum == "Evli" else 50

    # Kredi Notu Hesaplama
    kredi_notu = (
        (gelir_puan * 0.3) +
        ((ev_puan + araba_puan + arsa_puan) * 0.15) +  # Toplam varlık puanı
        (borc_puan * 0.15) +
        (calisma_puan * 0.2) +
        (egitim_puan * 0.1) +
        (medeni_puan * 0.1)
    )
    return round(kredi_notu)

# Kullanıcıdan girdi al
gelir = float(input("Aylık Gelir Düzeyinizi Girin (Örneğin: 54000): "))
ev_sayisi = int(input("Sahip Olduğunuz Ev Sayısını Girin (Örneğin: 1): "))
araba_sayisi = int(input("Sahip Olduğunuz Araba Sayısını Girin (Örneğin: 1): "))
arsa_sayisi = int(input("Sahip Olduğunuz Arsa Sayısını Girin (Örneğin: 0): "))
borc = float(input("Mevcut Borç Miktarınızı Girin (Örneğin: 7000): "))
calisma_yili = int(input("Toplam Çalışma Sürenizi Girin (Yıl olarak, Örneğin: 3): "))
egitim = input("Eğitim Düzeyinizi Girin (Ortaokul Mezunu, Lise Mezunu, Üniversite, Yüksek Lisans, Doktora): ").capitalize()
medeni_durum = input("Medeni Durumunuzu Girin (Evli veya Bekar): ").capitalize()

# Kredi notunu hesapla
kredi_notu = kredi_notu_hesapla(gelir, ev_sayisi, araba_sayisi, arsa_sayisi, borc, calisma_yili, egitim, medeni_durum)

# Sonucu göster
print(f"Hesaplanan Kredi Notunuz: {kredi_notu}")
