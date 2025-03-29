# -*- coding: utf-8 -*-
import os
from glob import glob
from AutoDockTools.MoleculePreparation import AD4LigandPreparation
from MolKit import Read

# Directorio donde están los péptidos en formato PDB
input_folder = "selected_peptides"
output_folder = "prepared_peptides"

# Crear carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Buscar archivos .pdb en la carpeta
pdb_files = glob(os.path.join(input_folder, "*.pdb"))

for pdb_file in pdb_files:
    try:
        print("Procesando {}...".format(pdb_file))
        mol = Read(pdb_file)[0]  # Cargar la molécula
        output_pdbqt = os.path.join(output_folder, os.path.basename(pdb_file).replace(".pdb", ".pdbqt"))

        # Preparar la molécula como ligando para AutoDock
        AD4LigandPreparation(mol, outputfilename=output_pdbqt)

        print("Guardado: {}".format(output_pdbqt))
    except Exception as e:
        print("Error con {}: {}".format(pdb_file, e))

print("Conversión completada.")
