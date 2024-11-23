import streamlit as st
import pandas as pd
import re

def ajouter_prefixe_vcf(contenu_vcf):
    """Ajoute '01' correctement pour les numéros Béninois dans un fichier VCF."""
    nouvelles_lignes = []
    for ligne in contenu_vcf.splitlines():
        if ligne.startswith("TEL"):
            numero = ligne.split(":")[1].strip()
            numero_modifie = traiter_numero(numero)
            ligne = f"TEL;TYPE=CELL:{numero_modifie}"
        nouvelles_lignes.append(ligne)
    return "\n".join(nouvelles_lignes)

def ajouter_prefixe_csv(df):
    """Ajoute '01' correctement pour les numéros Béninois dans un fichier CSV."""
    if 'phone' in df.columns:
        df['phone'] = df['phone'].apply(traiter_numero)
    return df

def traiter_numero(numero):
    """
    Traite un numéro de téléphone selon les règles :
    - Ajoute '01' uniquement pour les numéros Béninois.
    - Ne modifie pas les numéros avec d'autres indicatifs.
    """
    numero = numero.strip()

    # Cas 1 : Numéros internationaux commençant par +229
    if numero.startswith("+229"):
        local_part = numero[4:]  # Supprime "+229"
        if local_part.isdigit() and len(local_part) == 8:
            return f"+22901{local_part}"  # Ajoute "01" après "+229"
        return numero  # Ne modifie pas si incorrect

    # Cas 2 : Numéros locaux Béninois (8 chiffres)
    if numero.isdigit() and len(numero) == 8:
        return f"01{numero}"  # Ajoute "01" au début

    # Cas 3 : Autres indicatifs internationaux (ne pas modifier)
    if numero.startswith("+"):
        return numero

    # Cas 4 : Format inconnu ou incorrect (laisser tel quel)
    return numero

# Interface Streamlit
st.title("Modifier les numéros de téléphone")
st.write("Ajoutez '01' correctement aux numéros Béninois dans vos fichiers VCF ou CSV.")

# Chargement du fichier
uploaded_file = st.file_uploader("Choisissez un fichier (.vcf ou .csv)", type=["vcf", "csv"])

if uploaded_file:
    extension = uploaded_file.name.split('.')[-1].lower()
    
    if extension == 'vcf':
        contenu = uploaded_file.read().decode('utf-8')
        contenu_modifie = ajouter_prefixe_vcf(contenu)
        st.success("Fichier VCF modifié avec succès !")
        st.text_area("Contenu Modifié (Aperçu)", contenu_modifie, height=300)
        st.download_button("Télécharger le fichier modifié", contenu_modifie, file_name="contacts_modifies.vcf")

    elif extension == 'csv':
        df = pd.read_csv(uploaded_file)
        df_modifie = ajouter_prefixe_csv(df)
        st.success("Fichier CSV modifié avec succès !")
        st.dataframe(df_modifie)  # Affichage des données modifiées
        fichier_csv = df_modifie.to_csv(index=False)
        st.download_button("Télécharger le fichier modifié", fichier_csv, file_name="contacts_modifies.csv")

    else:
        st.error("Format non supporté. Veuillez importer un fichier .vcf ou .csv.")
