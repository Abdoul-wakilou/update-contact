# Gestionnaire de Numéros de Téléphone Béninois

Cette application permet d'ajouter automatiquement **"01"** devant les numéros de téléphone béninois tout en respectant les numéros étrangers. Elle prend en charge les fichiers **.csv** et **.vcf** (formats utilisés pour les contacts) et génère un fichier modifié prêt à être importé dans l'application Contacts de votre téléphone.

---

## Fonctionnalités

- Ajout de **"01"** devant les numéros béninois :
  - Numéros locaux (exemple : `51979163` devient `0151979163`).
  - Numéros avec indicatif Béninois (+229), où **"01"** est ajouté après l'indicatif (exemple : `+22962786175` devient `+2290162786175`).
- Préservation des numéros étrangers :
  - Les numéros commençant par des indicatifs internationaux autres que **+229** (ex. : **+33**, **+1**) restent inchangés.
- Supporte les fichiers **.csv** et **.vcf** :
  - CSV : Traitement des colonnes avec des numéros de téléphone.
  - VCF : Modification des entrées de contacts dans le format de carte virtuelle.
- Aperçu des modifications avant téléchargement.
- Téléchargement du fichier modifié en quelques clics.

---

## URL d'accès

Pour exécuter l'application localement :

Lorsque l'application est déployée, cette URL pourra être mise à jour pour indiquer l'adresse publique.

---

## Utilisation

### 1. Préparer le fichier des contacts

- Exportez vos contacts au format **.csv** ou **.vcf** depuis votre téléphone ou compte cloud (Google Contacts, iCloud, etc.).
  - **Fichier CSV** : Assurez-vous qu'il contient une colonne avec des numéros de téléphone (nommée `phone`).
  - **Fichier VCF** : Fichiers de type carte de visite électronique souvent générés par les téléphones ou applications de gestion des contacts.

### 2. Charger le fichier dans l'application

1. Accédez à l'application via l'URL fournie.
2. Cliquez sur **"Choisissez un fichier"**.
3. Importez votre fichier **.csv** ou **.vcf**.

### 3. Vérification et téléchargement

- L'application modifie automatiquement les numéros béninois :
  - Numéros locaux (8 chiffres) reçoivent **"01"** au début.
  - Numéros avec **+229** reçoivent **"01"** après l'indicatif.
  - Numéros étrangers ne sont pas modifiés.
- Aperçu des modifications :
  - **CSV** : Aperçu des nouvelles données dans un tableau interactif.
  - **VCF** : Aperçu du contenu modifié sous forme de texte.
- Téléchargez le fichier modifié :
  - Cliquez sur **"Télécharger le fichier modifié"**.
  - Le fichier sera enregistré sous le nom **contacts_modifies.csv** ou **contacts_modifies.vcf**.

### 4. Importer les nouveaux contacts dans votre téléphone

1. Téléchargez le fichier modifié depuis l'application.
2. Importez-le dans l'application Contacts de votre téléphone :
   - **Android** : Accédez aux paramètres des Contacts > Importer/Exporter > Importer depuis un fichier.
   - **iOS** : Utilisez iCloud ou AirDrop pour importer les contacts au format VCF.

---

## Exemples

### Fichier CSV avant modification :
```csv
name,phone
Jean,51979163
Paul,+3362786175
Marie,+22962786175
Luc,+22995123456
Alice,+123456789
