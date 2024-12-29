# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:13:10 2024

@author: YASEMIN
"""

def kredi_notu_hesapla(gelir, ev_sayisi, araba_sayisi, arsa_sayisi, borc, calisma_yili, egitim, medeni_durum):
    # Income Level Score
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
    
    # Number of Houses Score
    ev_puan = min(ev_sayisi * 100, 300)  # 100 points per house, maximum 300 points

    # Number of Cars Score
    araba_puan = min(araba_sayisi * 60, 180)   # 60 points per car, maximum 180 points

    # Number of Lands Score
    land_score = min(num_lands * 80, 240)  # 80 points per land, maximum 240 points

    # Debt Situation Score
    if debt == 0:
        debt_score = 2000
    elif debt < 10000:
        debt_score = 1000
    elif 10000 <= debt < 30000:
        debt_score = 500
    else:
        debt_score = 50

    # Work Experience Score
     if calisma_yili <= 5:
        calisma_puan = 500
    elif 6 <= calisma_yili <= 10:
        calisma_puan = 1000
    elif 11 <= calisma_yili <= 20:
        calisma_puan = 2000
    else:
        calisma_puan = 3000

    # Education Level Score
   egitim_puan = {
        "Ortaokul Mezunu": 50,
        "Lise Mezunu": 100,
        "Üniversite": 150,
        "Yüksek Lisans": 200,
        "Doktora": 250
    }.get(egitim, 0)

# Marital Status Score
medeni_puan = 100 if medeni_durum == "Evli" else 50

# Credit Score Calculation
kredi_notu = (
        (gelir_puan * 0.3) +
        ((ev_puan + araba_puan + arsa_puan) * 0.15) +  # Toplam varlık puanı
        (borc_puan * 0.15) +
        (calisma_puan * 0.2) +
        (egitim_puan * 0.1) +
        (medeni_puan * 0.1)
    )
    return round(kredi_notu)

# Get user input
gelir = float(input("Aylık Gelir Düzeyinizi Girin (Örneğin: 54000): "))
ev_sayisi = int(input("Sahip Olduğunuz Ev Sayısını Girin (Örneğin: 1): "))
araba_sayisi = int(input("Sahip Olduğunuz Araba Sayısını Girin (Örneğin: 1): "))
arsa_sayisi = int(input("Sahip Olduğunuz Arsa Sayısını Girin (Örneğin: 0): "))
borc = float(input("Mevcut Borç Miktarınızı Girin (Örneğin: 7000): "))
calisma_yili = int(input("Toplam Çalışma Sürenizi Girin (Yıl olarak, Örneğin: 3): "))
egitim = input("Eğitim Düzeyinizi Girin (Ortaokul Mezunu, Lise Mezunu, Üniversite, Yüksek Lisans, Doktora): ").capitalize()
medeni_durum = input("Medeni Durumunuzu Girin (Evli veya Bekar): ").capitalize()

# Calculate credit score
kredi_notu = kredi_notu_hesapla(gelir, ev_sayisi, araba_sayisi, arsa_sayisi, borc, calisma_yili, egitim, medeni_durum)

# Display the result
print(f"Hesaplanan Kredi Notunuz: {kredi_notu}")
