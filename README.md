# Convertisseur RTF vers TXT avec Split automatique

Bienvenue dans le projet **Convertisseur RTF vers TXT** ! 🚀

Ce projet est une application Python avec interface graphique (Tkinter) permettant de convertir facilement des fichiers **.RTF** en **.TXT**, avec la fonctionnalité intelligente de **spliter automatiquement** les fichiers volumineux en plusieurs parties si nécessaire.

---

## 🔍 Objectif du projet

Ce logiciel résout les problèmes suivants :
- Extraire le contenu brut de fichiers RTF en fichiers TXT lisibles.
- Gérer automatiquement les fichiers ayant plus de **100 000 caractères** en les divisant proprement en plusieurs parties.
- Proposer une interface graphique simple, sans besoin de connaissances techniques.

---

## 🔗 Fonctionnalités principales

- Conversion **RTF ➔ TXT** rapide et fiable.
- 🔎 **Analyse automatique** du nombre de caractères.
- 📊 **Split intelligent** des gros fichiers (à partir d'une limite définissable).
- ✨ Interface graphique ergonomique et moderne (Tkinter + ttk).
- ✅ Possibilité de traiter plusieurs fichiers en même temps.
- 📦 Création d'un éxécutable (.exe) pour Windows.

---

## 📝 Pré-requis

- Python 3.8 ou supérieur [https://www.python.org/](https://www.python.org/)
- pip (normalement installé avec Python)

Installer les librairies nécessaires avec :

```bash
pip install striprtf
pip install pyinstaller   # (optionnel pour créer un .exe)
```

---

## 📒 Installation et utilisation

### 1. Clonez le dépôt

```bash
git clone https://github.com/wesleypastana/Convertisseur-RTF-to-TXT.git
cd convertisseur_py
```

### 2. Lancez l'application

```bash
python interface_conversion.py
```

### 3. Créer un exécutable (facultatif)

Pour générer un .exe utilisable sans Python :

```bash
pyinstaller --onefile --noconsole --name ConvertRTF interface_conversion.py
```

Votre fichier `ConvertRTF.exe` sera créé dans le dossier `/dist/`.

---

## 🌐 Utilisation de l'application

1. **Ajouter fichiers** : Cliquez pour ajouter un ou plusieurs fichiers `.rtf`.
2. **Choisir dossier de destination** : Définissez où sauvegarder les fichiers convertis.
3. **Configurer options** (facultatif) :
   - Activer ou désactiver le split automatique.
   - Choisir le nombre maximum de caractères avant division.
4. **Démarrer la conversion** : Cliquez sur "Démarrer Conversion".
5. Vos fichiers .txt seront générés dans le dossier choisi, avec split automatique si nécessaire.

---

## 📊 Exemple

- Un fichier de 250 000 caractères sera automatiquement divisé en 3 fichiers :
  - `MonDocument_Part1.txt`
  - `MonDocument_Part2.txt`
  - `MonDocument_Part3.txt`

Chaque partie ayant à peu près le même nombre de caractères.

---

## 👨‍💻 Auteurs

- Projet développé par Wesley PASTANA

---

## 🚫 Licence

Projet sous licence **MIT** - libre d'utilisation, de modification et de distribution.