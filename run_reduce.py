import os
import subprocess

# Ruta de la carpeta que contiene los peptidos
input_dir = "selected_peptides"
output_dir = "reduced_peptides"

# Asegurar que el directorio de salida existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Ruta al ejecutable reduce de ADFRsuite
reduce_exe = "/Users/paschalogbogu/docking/ADFRsuite_x86_64Darwin_1.0/exec/bin/reduce"

# Obtener la lista de archivos PDB en la carpeta de entrada
peptide_files = [f for f in os.listdir(input_dir) if f.endswith(".pdb")]

for peptide_file in peptide_files:
    # Obtener el nombre del peptido sin extension
    peptide_name = os.path.splitext(peptide_file)[0]
    
    # Crear directorio de salida para este peptido
    peptide_output_dir = os.path.join(output_dir, peptide_name)
    if not os.path.exists(peptide_output_dir):
        os.makedirs(peptide_output_dir)
    
    # Definir archivo de salida
    output_file = os.path.join(peptide_output_dir, "{}_pepH.pdb".format(peptide_name))
    
    # Ejecutar reduce
    cmd = [reduce_exe, "-FLIP", os.path.join(input_dir, peptide_file)]
    with open(output_file, "w") as out_f:
        subprocess.call(cmd, stdout=out_f)

    print("Procesado: {}".format(peptide_file))

print("Reduccion completada.")
