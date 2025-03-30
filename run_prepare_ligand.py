import os
import subprocess

# Ruta del ejecutable prepare_ligand.py
prepare_ligand_exe = "/Users/paschalogbogu/docking/ADFRsuite_x86_64Darwin_1.0/exec/bin/prepare_ligand.py"

# Carpeta de entrada y salida
input_dir = "reduced_peptides"
output_dir = "prepared_peptides"

# Asegurar que la carpeta de salida existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Recorrer subcarpetas dentro de reduced_peptides
for peptide_folder in os.listdir(input_dir):
    peptide_path = os.path.join(input_dir, peptide_folder)
    
    if os.path.isdir(peptide_path):  # Asegurar que es un directorio
        # Buscar archivos PDB dentro de la subcarpeta
        for filename in os.listdir(peptide_path):
            if filename.endswith("_H.pdb"):
                input_pdb = os.path.join(peptide_path, filename)
                
                # Crear la carpeta de salida para este peptido
                peptide_output_dir = os.path.join(output_dir, peptide_folder)
                if not os.path.exists(peptide_output_dir):
                    os.makedirs(peptide_output_dir)

                # Definir el nombre de salida
                output_pdbqt = os.path.join(peptide_output_dir, filename.replace(".pdb", ".pdbqt"))

                # Comando para ejecutar prepare_ligand.py
                cmd = ["python", prepare_ligand_exe, "-l", input_pdb, "-o", output_pdbqt]

                print("Ejecutando:", " ".join(cmd))

                # Ejecutar el comando
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                # Manejo de errores
                if process.returncode != 0:
                    print(f"Error procesando {input_pdb}:\n{stderr.decode()}")

print("Proceso completado.")
