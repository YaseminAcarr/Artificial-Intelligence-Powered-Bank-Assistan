# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:30:18 2024

@author: ZEYNEP
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from scipy import stats

# Verilerin yüklenmesi
veriler = pd.read_excel('bankaverileri_smote.xlsx')

# Eksik verileri tespit etme ve doldurma
print("Eksik veri sayısı (her sütun için):")
print(veriler.isnull().sum())

# Sayısal sütunları doldurmak için SimpleImputer kullanımı
sayisal_sutunlar = veriler.select_dtypes(include=['float64', 'int64']).columns
imputer_sayisal = SimpleImputer(strategy='mean')  # Ortalama ile doldurma
veriler[sayisal_sutunlar] = imputer_sayisal.fit_transform(veriler[sayisal_sutunlar])

# Kategorik sütunları doldurmak için SimpleImputer kullanımı
kategorik_sutunlar = veriler.select_dtypes(include=['object']).columns
imputer_kategorik = SimpleImputer(strategy='most_frequent')  # En sık tekrar eden değer ile doldurma
veriler[kategorik_sutunlar] = imputer_kategorik.fit_transform(veriler[kategorik_sutunlar])

# Eksik veri kontrolü sonrası
print("\nEksik veri kontrolü sonrası (her sütun için):")
print(veriler.isnull().sum())

# Kategorik sütunları sayısallaştırma
label_encoders = {}
for column in ['Cinsiyet', 'Meslek', 'Eğitim Düzeyi', 'Medeni Durum', 'Konut', 'Araç', 'Arsa']:
    le = LabelEncoder()
    veriler[column] = le.fit_transform(veriler[column].astype(str))
    label_encoders[column] = le  # Encoderları saklıyoruz

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirleme
X = veriler.drop(columns=['Kredi Notu'])  # 'Kredi Notu' dışındaki tüm sütunları bağımsız değişken olarak alıyoruz
y = veriler['Kredi Notu']  # 'Kredi Notu' bağımlı değişken olarak alıyoruz

# Verileri %75 eğitim ve %25 test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# **Özellik Standardizasyonu** (Ölçeklendirme)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Eğitim verisini ölçeklendir
X_test_scaled = scaler.transform(X_test)  # Test verisini ölçeklendir

# **Ağaç Modelini Geliştirme** (Daha fazla ağaç, derinliği artırma, min_samples_split ve min_samples_leaf optimizasyonu)
random_forest_model = RandomForestRegressor(
    random_state=0, 
    n_estimators=200,  # Ağaç sayısını artırdık
    max_depth=10,  # Derinliği azaltmak yerine bu değeri artırdık
    min_samples_split=5,  # Min. split değeri daha büyük
    min_samples_leaf=2,  # Min. leaf sayısını artırarak daha sağlam ağaçlar
    n_jobs=-1  # İşlemci çekirdeklerini tam verimli kullanmak için
)

# Modeli eğitme
random_forest_model.fit(X_train_scaled, y_train)

# Test verisi ile kredi notlarını tahmin etme
y_pred_rf = random_forest_model.predict(X_test_scaled)

# Model performansını değerlendirme (Random Forest)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("\nRandom Forest - Test Verisi MSE (Standardize Edilmiş):", mse_rf)
print("Random Forest - Test Verisi R² Skoru (Standardize Edilmiş):", r2_rf)

# Linear Regression modelini oluşturma ve eğitme
linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)

# Test verisi ile kredi notlarını tahmin etme
y_pred_lr = linear_model.predict(X_test_scaled)

# Model performansını değerlendirme (Linear Regression)
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print("\nLinear Regression - Ortalama Kare Hata (MSE):", mse_lr)
print("Linear Regression - R-Kare (R²) Skoru:", r2_lr)
