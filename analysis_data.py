import pandas as pd
import matplotlib.pyplot as plt

# Chemin du fichier
file_path = r""

# Chargement des données
data = pd.read_csv(file_path)

# Conversion des colonnes "Date" et "Heure" en une seule colonne datetime
data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Heure'], format='%d/%m/%Y %H:%M')

# Suppression des colonnes originales Date et Heure
data = data.drop(['Date', 'Heure'], axis=1)

# Affichage des informations sur les données
print("Aperçu des données après transformation :")
print(data.head())

# Visualisation 1 : Radiation Solaire Globale au cours du temps
plt.figure(figsize=(15, 6))
plt.plot(data['Datetime'], data['Radiation solaire globale '], label="Radiation Solaire Globale", linewidth=0.7)
plt.title("Évolution de la Radiation Solaire Globale au cours du temps", fontsize=14)
plt.xlabel("Temps", fontsize=12)
plt.ylabel("Radiation Solaire Globale", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Visualisation 2 : Température au cours du temps
plt.figure(figsize=(15, 6))
plt.plot(data['Datetime'], data['Temperature '], color='orange', label="Température", linewidth=0.7)
plt.title("Évolution de la Température au cours du temps", fontsize=14)
plt.xlabel("Temps", fontsize=12)
plt.ylabel("Température (°C)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Visualisation 3 : Azimuth Angle et Solar Elevation au cours du temps
plt.figure(figsize=(15, 6))
plt.plot(data['Datetime'], data['Azimuth Angle'], label="Azimuth Angle", linewidth=0.7)
plt.plot(data['Datetime'], data['Solar Elevation'], label="Solar Elevation", linewidth=0.7)
plt.title("Évolution des Angles Solaires au cours du temps", fontsize=14)
plt.xlabel("Temps", fontsize=12)
plt.ylabel("Angle (degrés)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Export des statistiques descriptives sous forme de tableau
description = data.describe()

# Sauvegarde du tableau descriptif dans un fichier Excel
description_file = r""
description.to_excel(description_file)

print(f"Les statistiques descriptives ont été exportées vers : {description_file}")
