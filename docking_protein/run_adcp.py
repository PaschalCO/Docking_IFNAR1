import os
import subprocess

# Directorio base donde estan las carpetas de los peptidos
base_dir = "reduced_peptides"

# Ruta al script runADCP de ADFRsuite
run_adcp_path = "/Users/paschalogbogu/docking/ADFRsuite_x86_64Darwin_1.0/exec/CCSBpckgs/ADCP/runADCP.py"

# Verifica si el directorio base existe
if not os.path.exists(base_dir):
    print("Error: El directorio {} no existe.".format(base_dir))
    exit(1)

# Recorre todas las carpetas dentro de reduced_peptides
for peptide_folder in os.listdir(base_dir):
    peptide_path = os.path.join(base_dir, peptide_folder)
    
    # Verifica si es un directorio
    if os.path.isdir(peptide_path):
        trg_file = os.path.join(peptide_path, "{}.trg".format(peptide_folder))
        output_folder = "{}_docking".format(peptide_folder)

        # Verifica si el archivo .trg existe en la carpeta
        if os.path.exists(trg_file):
            command = [
                "python", run_adcp_path,
                "-t", "{}.trg".format(peptide_folder),
                "-s", "npisdvd",
                "-N", "20",
                "-n", "1000000",
                "-o", output_folder,
                "-ref", "{}_pepH.pdb".format(peptide_folder)
            ]

            print("Ejecutando en {}: {}".format(peptide_path, " ".join(command)))
            try:
                subprocess.call(command, cwd=peptide_path)  # Ejecutar en el directorio del peptido
            except Exception as e:
                print("Error procesando {}: {}".format(peptide_folder, e))
        else:
            print("Error: No se encontro {} en {}".format(trg_file, peptide_folder))
