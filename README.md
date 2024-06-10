# ELEC-400
Dossier pour les étudiants du cours ELEC-400

# Interaction avec Firebase Firestore en Utilisant Python

## Introduction

Ce projet vous permet d'interagir avec une base de données Firebase Firestore en utilisant Python. Vous pourrez ajouter, lire, mettre à jour et supprimer des documents dans la base de données directement à partir de vos scripts Python.

## Prérequis

- Python installé sur votre machine
- Accès au fichier de clé JSON du compte de service Firebase
- Connaissances de base en Python et en utilisation de la ligne de commande

## Étapes pour Configurer et Utiliser le Projet

### 1. Configuration de Firebase

#### a. Créer un Projet Firebase

1. Allez sur la [console Firebase](https://console.firebase.google.com/).
2. Cliquez sur "Add project" (Ajouter un projet) et suivez les instructions pour créer un nouveau projet.

#### b. Configurer Firestore

1. Dans la console Firebase, allez à "Database" (Base de données) dans le menu de gauche.
2. Cliquez sur "Create database" (Créer une base de données).
3. Choisissez "Start in test mode" (Démarrer en mode test) pour initialiser Firestore.

#### c. Télécharger la Clé d'authentification

1. Dans les paramètres du projet (icône d'engrenage), allez à "Service accounts" (Comptes de service).
2. Cliquez sur "Generate new private key" (Générer une nouvelle clé privée).
3. Téléchargez le fichier JSON et placez-le dans le même répertoire que votre script Python puis renommer la pour que cela corresponde avec le code python.

### 2. Installer les Bibliothèques Nécessaires

1. Ouvrez un terminal ou une invite de commande.
2. Activez votre environnement virtuel (si vous en utilisez un) et installez `firebase-admin` :

   ```bash
   pip install firebase-admin
   ````


### 3. Configurer le Script Python

1. Placez le fichier de clé JSON dans le même répertoire que votre script Python.
2. Mettez à jour le chemin du fichier de clé JSON dans le script Python.

### 4. Utilisation du Script

#### Ajouter un document 

Pour ajouter un document à la collection 
`your_collection`,
exécutez le script. Modifiez la fonction add_document pour ajouter les données souhaitées.

La fonction est la suivante : 

```python
if __name__ == "__main__":
    get_document("your_document_id")
```
#### Récupérer un Document

Pour récupérer un document de la collection your_collection :

```python 
if __name__ == "__main__":
    get_document("your_document_id")
```

#### Mettre à Jour un Document

Pour mettre à jour un document :

```python 
if __name__ == "__main__":
    update_document("your_document_id", {"field1": "new_value"})
```

## Structure de la base de donnée

Pour que l'application bypark puisse communiquer avec votre système de verroullage et dévérouillage il faut que nous utilisions les mêmes champs pour la base de donnée. Pour cela, il faut créer 4 collections contenant chacun des documents qui contiennent eux mêmes des champs. (Si vous souhaitez ajouter ou supprimer des éléments dans votre base de donnée j'aimerais que cela soit expliqué) :

## Structure de la Collection `users`

### Champs des Documents

Chaque document dans la collection `users` contient les champs suivants :

- **box_occupied** : Un entier représentant le numéro de la box occupé par l'utilisateur. 
  - Type : `Integer`
  - Exemple : `0`

- **email** : L'adresse e-mail de l'utilisateur.
  - Type : `String`
  - Exemple : `"eleve@ens.etsmtl.ca"`

- **fullName** : Le nom complet de l'utilisateur.
  - Type : `String`
  - Exemple : `"eleve"`

- **id** : L'identifiant unique du document (généré automatiquement par Firestore).
  - Type : `String`
  - Exemple : `"8wG20jC7MTWZzGvSWZN47otAsdK2"`

- **rented_box** : Un booléen indiquant si l'utilisateur a loué un box.
  - Type : `Boolean`
  - Exemple : `false`

- **rfid_card_id** : L'identifiant unique de la carte RFID associée à l'utilisateur.
  - Type : `String`
  - Exemple : `"RFID123456"`

## Exemple de Document

Un document typique dans la collection `users` ressemble à ceci :

```json
{
  "box_occupied": 0,
  "email": "eleve@ens.etsmtl.ca",
  "fullName": "eleve",
  "id": "8wG20jC7MTWZzGvSWZN47otAsdK2",
  "rented_box": false,
  "rfid_card_id": "RFID123456"
}
```

## Utilisation des données

### Ajouter un Utilisateur :

Pour ajouter un utilisateur à la collection users, utilisez la fonction add_document dans votre script Python :

```Python 
if __name__ == "__main__":
    add_document({
        "box_occupied": 0,
        "email": "nouveau@example.com",
        "fullName": "Nouveau Utilisateur",
        "rented_box": false,
        "rfid_card_id": "RFID789101"
    })
```

### Récupérer un Utilisateur

Pour récupérer les informations d'un utilisateur, utilisez la fonction get_document avec l'identifiant du document :

```python 
if __name__ == "__main__":
    get_document("id_du_document")
```

### Mettre à Jour un Utilisateur
Pour mettre à jour les informations d'un utilisateur, utilisez la fonction update_document avec l'identifiant du document et les nouvelles données :

```python 
if __name__ == "__main__":
    update_document("id_du_document", {
        "box_occupied": 1,
        "rented_box": true
    })
```

## Structure de la Collection `box`

### Champs des Documents

Chaque document dans la collection `box` contiendra les champs suivants :

- **box_id** : Un entier représentant l'ID unique du box.
  - Type : `Integer`
  - Exemple : `1`

- **occupants** : Une liste contenant les IDs des utilisateurs occupant le box. S'il n'y a pas d'occupants, cette liste est vide.
  - Type : `Array of Strings`
  - Exemple : `[]`

- **occupied** : Un booléen indiquant si le box est actuellement occupé. Cette valeur est `true` si le nombre d'occupants atteint la capacité maximale (8).
  - Type : `Boolean`
  - Exemple : `false`

- **capacity** : Le nombre total de places disponibles dans le box.
  - Type : `Integer`
  - Exemple : `8`

- **ip_address** : L'adresse IP de la station à laquelle le box est rattaché.
  - Type : `String`
  - Exemple : `"127.0.0.1"`

- **latitude** : La latitude de la station à laquelle le box est rattaché.
  - Type : `Double`
  - Exemple : `43`

- **longitude** : La longitude de la station à laquelle le box est rattaché.
  - Type : `Double`
  - Exemple : `7`

- **station_name** : Le nom de la station à laquelle le box est rattaché.
  - Type : `String`
  - Exemple : `"Boulevard de Montréal"`

## Exemple de Document

Un document typique dans la collection `box` ressemble à ceci :

```json
{
  "box_id": 1,
  "occupants": [],
  "occupied": false,
  "capacity": 8,
  "ip_address": "127.0.0.1",
  "latitude": 43,
  "longitude": 7,
  "station_name": "Boulevard de Montréal"
}
```
## Utilisation des Données

### Ajouter un Box
Pour ajouter un box à la collection box, utilisez la fonction add_document dans votre script Python :

```python
if __name__ == "__main__":
    add_document({
        "box_id": 1,
        "occupants": [],
        "occupied": false,
        "capacity": 8,
        "ip_address": "127.0.0.1",
        "latitude": 43,
        "longitude": 7,
        "station_name": "Boulevard de Montréal"
    })
```

### Récupérer un Box

Pour récupérer les informations d'un box, utilisez la fonction get_document avec l'identifiant du document :

```python
if __name__ == "__main__":
    get_document("id_du_document")
```

### Mettre à Jour un Box
Pour mettre à jour les informations d'un box, utilisez la fonction update_document avec l'identifiant du document et les nouvelles données :


```python
if __name__ == "__main__":
    update_document("id_du_document", {
        "occupants": ["user1", "user2"],  # Ajoutez les occupants actuels
        "occupied": len(["user1", "user2"]) == 8  # Vérifiez si le box est plein
    })
```

## Introduction

Cette documentation explique comment interagir avec la collection `reservations` dans Firebase Firestore. La collection `reservations` contient des documents représentant les réservations des boxes.

## Structure de la Collection `reservations`

### Champs des Documents

Chaque document dans la collection `reservations` contiendra les champs suivants :

- **box_id** : Un entier représentant l'ID unique du box réservé.
  - Type : `Integer`
  - Exemple : `1`

- **endDate** : La date et l'heure de fin de la réservation.
  - Type : `Timestamp`
  - Exemple : `"13 février 2024 à 09:30:47 UTC-5"`

- **startTime** : La date et l'heure de début de la réservation.
  - Type : `Timestamp`
  - Exemple : `"13 février 2024 à 09:30:47 UTC-5"`

- **userID** : L'ID de l'utilisateur ayant fait la réservation.
  - Type : `String`
  - Exemple : `"a9YCoCQKwdX8bisZdXvBv6W2lE02"`

## Exemple de Document dans la Collection `reservations`

Un document typique dans la collection `reservations` ressemble à ceci :

```json
{
  "box_id": 1,
  "endDate": "13 février 2024 à 09:30:47 UTC-5",
  "startTime": "13 février 2024 à 09:30:47 UTC-5",
  "userID": "a9YCoCQKwdX8bisZdXvBv6W2lE02"
}
```


## Utilisation des Données dans la Collection reservations

### Ajouter une Réservation
Pour ajouter une réservation à la collection reservations, utilisez la fonction add_document dans votre script Python :

```python
if __name__ == "__main__":
    add_document({
        "box_id": 1,
        "endDate": "13 février 2024 à 09:30:47 UTC-5",
        "startTime": "13 février 2024 à 09:30:47 UTC-5",
        "userID": "a9YCoCQKwdX8bisZdXvBv6W2lE02"
    })
```
### Récupérer une Réservation
Pour récupérer les informations d'une réservation, utilisez la fonction get_document avec l'identifiant du document :

```python
if __name__ == "__main__":
    get_document("id_du_document")
```

### Mettre à Jour une Réservation
Pour mettre à jour les informations d'une réservation, utilisez la fonction update_document avec l'identifiant du document et les nouvelles données :

```python
if __name__ == "__main__":
    update_document("id_du_document", {
        "endDate": "14 février 2024 à 10:00:00 UTC-5"
    })
```

` Bonne chance dans l'utilisation de Firebase Firestore pour votre projet ! N'hésitez pas à me contacter en cas de problèmes ou de questions. Je suis là pour vous aider. Vous pouvez me joindre par email ou réserver un créneau. Travaillez bien et bon courage !`
