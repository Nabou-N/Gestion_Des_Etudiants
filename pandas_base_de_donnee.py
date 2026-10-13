from pathlib import Path
import pandas as pd
import numpy as np

FICHIER = Path("./document/notes_etudiant_exemple.xlsx")

df = pd.ExcelFile(FICHIER, engine="openpyxl")
# print("=========df.sheet_names")
# print(df.sheet_names)

etudiants = pd.read_excel(FICHIER, sheet_name="Etudiants",engine="openpyxl")
notes = pd.read_excel(FICHIER, sheet_name="Notes",engine="openpyxl")
# inscriptions = pd.read_excel(FICHIER, sheet_name="Inscriptions",engine="openpyxl")

def nettoyer_colonnes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("'", "", regex=False)
    )
    return df

etudiants_clair = nettoyer_colonnes(etudiants)
notes_clair = nettoyer_colonnes(notes)


print("=========etudiants")
print(etudiants_clair.head())
# print("=========notes_clair")
# print(notes_clair.head())