import os
from Bio import PDB

# Ruta donde estan almacenadas las carpetas de peptidos
base_dir = "pepbdb-20200318/pepbdb"

# Inicializa el parser de PDB
parser = PDB.PDBParser(QUIET=True)
seq_dict = {}

for folder in os.listdir(base_dir):
    peptide_pdb = os.path.join(base_dir, folder, "peptide.pdb")
    
    if os.path.exists(peptide_pdb) and os.path.getsize(peptide_pdb) > 0:  # Verifica si el archivo no está vacio
        try:
            structure = parser.get_structure(folder, peptide_pdb)
            sequence = ""
            residues_found = 0  # Contador de residuos validos
            chain_id = None  # Almacenar el ID de la cadena detectada

            for model in structure:
                for chain in model:
                    if chain_id is None:  # Solo seleccionamos la primera cadena detectada
                        chain_id = chain.id
                    
                    if chain.id == chain_id:  # Asegurar que no estamos tomando residuos de varias cadenas
                        for residue in chain:
                            if PDB.is_aa(residue, standard=True):  # Solo considera aminoacidos estandar
                                try:
                                    sequence += PDB.Polypeptide.three_to_one(residue.resname)
                                    residues_found += 1  # Contar residuos validos
                                except KeyError:
                                    print(f"Residuo desconocido en {folder}: {residue.resname}")

            if residues_found > 0:
                seq_dict[folder] = sequence  # Solo guardar si hay residuos validos
            else:
                print(f"{folder}: No se encontraron aminoácidos válidos en la estructura.")

        except Exception as e:
            print(f"Error procesando {peptide_pdb}: {e}")

# Guarda las secuencias en un archivo FASTA
with open("pepbdb_sequences.fasta", "w") as fasta_file:
    for name, seq in seq_dict.items():
        fasta_file.write(f">{name}\n{seq}\n")

print("Se ha generado el archivo pepbdb_sequences.fasta correctamente.")
