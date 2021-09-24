Sequence = "tatgctttcc#tataggtctg#ctattcaatg"
dna_list = Sequence.split("#")
print(dna_list)

for dna in dna_list:
    rna = dna.replace("t", "u")
    print(f"DNA: {dna} -> RNA: {rna}")