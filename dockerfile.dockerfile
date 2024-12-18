# Utilise l'image Python comme base
FROM python:3.8-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tous les autres fichiers (y compris app.py) dans le conteneur
COPY . .

# Expose le port 5000 pour Flask
EXPOSE 5000

# Lance l'application Flask
CMD ["python", "app.py"]

