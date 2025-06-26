# Import necessary libraries
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE


# Load the data
file_path = 'bankaverileri.xlsx'  # Path to your file
data = pd.read_excel(file_path)

# Fill missing values
data.fillna(data.mean(numeric_only=True), inplace=True)
categorical_cols = data.select_dtypes(include=['object']).columns
data[categorical_cols] = data[categorical_cols].fillna("Bilinmiyor")

# Data type check and adjustment
for col in categorical_cols:
    data[col] = data[col].astype(str)  # Convert all categorical values to strings

# Categorize 'Credit Score'  (Düşük: <1000, Orta: 1000-1200, Yüksek: >1200)
bins = [0, 1000, 1200, float('inf')]
labels = ['Düşük', 'Orta', 'Yüksek']
data['Kredi Notu Kategori'] = pd.cut(data['Kredi Notu'], bins=bins, labels=labels)

# Select only numerical variables and the target for SMOTE
numerical_cols = data.select_dtypes(include=['number']).columns
X_numerical = data[numerical_cols]   # Select only numerical variables
y = data['Kredi Notu Kategori']  # Target variable

# Perform SMOTE

try:
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_numerical, y)
except Exception as e:
    print(f"SMOTE işlemi sırasında bir hata oluştu: {e}")
    raise

# Round fractional values to integers
X_resampled = np.round(X_resampled).astype(int)

# Create a new dataset: Add categorical columns
resampled_data = pd.DataFrame(X_resampled, columns=numerical_cols)
resampled_data['Kredi Notu Kategori'] = y_resampled

# Add original categorical columns
for col in categorical_cols:
    # Repeat original data to match the length of resampled_data
    resampled_data[col] = np.tile(data[col].values, len(resampled_data) // len(data[col]) + 1)[:len(resampled_data)]
   # Add categorical columns as they are, repeating original data to match the length

# Save the results
output_file = 'bankaverileri_smote.xlsx'
resampled_data.to_excel(output_file, index=False)

print(f"SMOTE işlemi tamamlandı. Yeni veri '{output_file}' dosyasına kaydedildi.")
