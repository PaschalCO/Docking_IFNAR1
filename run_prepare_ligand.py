import os
import subprocess

# Directorio donde estan las carpetas de los peptidos (ruta absoluta o relativa correcta)
base_dir = "reduced_peptides"

# Recorre todas las carpetas dentro de reduced_peptides
for peptide_folder in os.listdir(base_dir):
    peptide_path = os.path.join(base_dir, peptide_folder)
    
    # Verifica si es un directorio
    if os.path.isdir(peptide_path):
        
        # Busca archivos que terminan en '_pepH.pdb'
        for file in os.listdir(peptide_path):
            if file.endswith("_pepH.pdb"):
                pdb_file = os.path.join(peptide_path, file)

                # Verifica si el archivo realmente existe
                if os.path.exists(pdb_file):
                    # Ejecuta prepare_ligand dentro de la ruta del peptido
                    command = ["prepare_ligand", "-l", file]
                    print("Ejecutando: {} en {}".format(' '.join(command), peptide_path))
                    try:
                        subprocess.call(command, cwd=peptide_path)  # Utiliza 'cwd' para ejecutar en el directorio correcto
                    except Exception as e:
                        print("Error procesando {}: {}".format(file, e))
                else:
                    print("El archivo {} no existe en {}.".format(pdb_file, peptide_path))
