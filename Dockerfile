# Tu peux utiliser une version existante de Python, par ex. 3.12
FROM python:3.14

# Dossier de travail dans le conteneur
WORKDIR /opt/hello_world/

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier ton script dans le dossier de travail
COPY hello_world.py .

EXPOSE 80

# Lancer le script Python
CMD ["python", "hello_world.py"]
