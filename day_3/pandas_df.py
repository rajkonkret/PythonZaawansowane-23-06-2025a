import pandas as pd

# pola.rs
# dask
# Spark
data = {
    "Imie": ["Jan", 'Piotr', 'Inga', 'Anna'],
    "Wiek": [34, 21, 39, 18],
    "Miasto": ["Warszawa", 'Gdańsk', "Lublin", "Kraków"]
}

df = pd.DataFrame(data)
print(df)
#     Imie  Wiek    Miasto
# 0    Jan    34  Warszawa
# 1  Piotr    21    Gdańsk
# 2   Inga    39    Lublin
# 3   Anna    18    Kraków

print("_" * 60)
filtered_df = df[df['Wiek'] > 30]
print(filtered_df)
# ____________________________________________________________
#    Imie  Wiek    Miasto
# 0   Jan    34  Warszawa
# 2  Inga    39    Lublin

mean_age = df['Wiek'].mean()
print(f"Sredni wiek: {mean_age} lat")  # Sredni wiek: 28.0 lat

df.to_csv('dane.csv', index=False, encoding='utf-8')
