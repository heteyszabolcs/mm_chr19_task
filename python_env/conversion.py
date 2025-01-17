from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def dna_to_protein_fasta(input_fasta, output_fasta):
    """
    Converting DNA fasta to Protein fasta by translating sequences.

    Args:
        input_fasta (str): Path to the input DNA fasta coming from the bedtools.
        output_fasta (str): Path to the output Protein fasta file.
    """
    protein_records = []

    # Parse the input fasta file
    for record in SeqIO.parse(input_fasta, "fasta"):
        # Translate the DNA sequence to a aminoacid sequence
        # to_stop argument: if True translation is terminated at the first in frame stop codon
        protein_seq = record.seq.translate(to_stop=True)

        # Create a new SeqRecord for the protein sequence
        protein_record = SeqRecord(
            protein_seq,
            id=record.id,
            description="Translated from DNA"
        )

        protein_records.append(protein_record)

    # Write the protein sequences to the output FASTA file
    SeqIO.write(protein_records, output_fasta, "fasta")
    print(f"Protein FASTA file saved to {output_fasta}")

# run
input_fasta = "../output/assembly.fa"  # Replace with your input DNA FASTA file path
output_fasta = "../output/assembly_aa.fa"  # Replace with desired output file path
dna_to_protein_fasta(input_fasta, output_fasta)
