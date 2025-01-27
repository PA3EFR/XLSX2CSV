"""
This file was created and tested by Erwin - PA3EFR
"""


import pandas as pd

def xlsx_to_csv_with_combined_columns(input_file, output_file, columns, combine_columns, new_column_name, separator=" "):
    """
    Converteert een XLSX-bestand naar een CSV-bestand met samengevoegde kolommen en geselecteerde kolommen.
    
    Parameters:
    - input_file: Pad naar het invoer XLSX-bestand.
    - output_file: Pad waar het CSV-bestand wordt opgeslagen.
    - columns: Lijst van kolomnamen of indexen die in het CSV-bestand moeten worden opgenomen.
    - combine_columns: Tuple of lijst met twee kolomnamen om samen te voegen.
    - new_column_name: Naam van de nieuwe kolom na het samenvoegen.
    - separator: Scheidingsteken tussen de samengevoegde waarden (standaard is een spatie).
    """
    try:
        # Lees het Excel-bestand
        df = pd.read_excel(input_file)
        
        # Controleer of de kolommen bestaan
        if not all(col in df.columns for col in combine_columns):
            raise ValueError("Een of beide kolommen om samen te voegen bestaan niet in het bestand.")
        
        # Voeg de kolommen samen
        df[new_column_name] = df[combine_columns[0]].astype(str) + separator + df[combine_columns[1]].astype(str)
        
        # Selecteer de gewenste kolommen inclusief de nieuwe kolom
        selected_columns = df[columns]
        
        # Schrijf naar CSV
        selected_columns.to_csv(output_file, index=False)
        
        print(f"CSV-bestand succesvol opgeslagen naar: {output_file}")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

# Voorbeeldgebruik
# Vervang deze waarden door je eigen bestandsnamen en kolomnamen
input_file = "Overzicht_JOTA_QTHs.xlsx"
output_file = "Overzicht_JOTA_QTHs.csv"
combine_columns = ("Jaartal", "Info")  # Kolommen om samen te voegen
new_column_name = "JOTA"  # Naam van de nieuwe kolom
columns = ["JOTA", "Latitude", "Longitude"]  # Gewenste kolommen in de CSV
separator = ": "  # Scheidingsteken tussen de samengevoegde kolommen

xlsx_to_csv_with_combined_columns(input_file, output_file, columns, combine_columns, new_column_name, separator)
