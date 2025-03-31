import os
import subprocess

# Directorio donde estan las carpetas de los peptidos
base_dir = "reduced_peptides"

# Archivo receptor (ya esta en el directorio actual)
receptor_file = "3s98_without_K_H.pdbqt"

# Directorio donde se encuentra 'runAGFR.py'
run_agfr_path = "/Users/paschalogbogu/docking/ADFRsuite_x86_64Darwin_1.0/exec/CCSBpckgs/ADFR/bin/runAGFR.py"

# Verifica si el directorio base existe
if not os.path.exists(base_dir):
    print("Error: El directorio {} no existe.".format(base_dir))
    exit(1)

# Recorre todas las carpetas dentro de reduced_peptides
for peptide_folder in os.listdir(base_dir):
    peptide_path = os.path.join(base_dir, peptide_folder)
    
    # Verifica si es un directorio
    if os.path.isdir(peptide_path):
        
        # Busca archivos que terminan en '_H.pdbqt' para los ligandos
        for file in os.listdir(peptide_path):
            if file.endswith("_pepH.pdbqt"):
                pdbqt_file = file  # El nombre del archivo del ligando

                # Verificar si el archivo del ligando y el receptor existen
                if os.path.exists(receptor_file) and os.path.exists(os.path.join(peptide_path, pdbqt_file)):
                    # Construir el comando para ejecutar dentro de la carpeta del peptido
                    command = [
                        "python", 
                        run_agfr_path,
                        "-r", receptor_file,  # Receptor siempre esta en el directorio actual
                        "-l", pdbqt_file,      # Ligando es el archivo correspondiente en la carpeta del peptido
                        "-asv", "1.1",
                        "-o", peptide_folder
                    ]
                    
                    # Ejecutar el comando en el directorio del peptido usando 'cwd'
                    print("Ejecutando: {}".format(" ".join(command)))
                    try:
                        subprocess.call(command, cwd=peptide_path)  # Ejecutar en el directorio del peptido
                    except Exception as e:
                        print("Error procesando {}: {}".format(pdbqt_file, e))
                else:
                    print("Faltan archivos para el peptido en {}: {} o {}".format(peptide_folder, receptor_file, pdbqt_file))
