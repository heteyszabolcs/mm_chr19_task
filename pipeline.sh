#!/bin/bash -l

# modules
module load bowtie
module load stringtie
module load bedtools

# variables
DIR="/cfs/klemming/projects/snic/snic2020-6-3/SZABOLCS/Lethio_group"
OUTPUT_DIR="output"
REFERENCE_DIR="reference"
REFERENCE_FASTA="reference/Mus_musculus.GRCm38.dna.chromosome.19.fa"
INPUT="bam/mouse_chr19.bam"

cd ${DIR}

## pipeline
# stringtie
echo "assembly is running"
stringtie -o ${OUTPUT_DIR}/assembly.gtf --rf \
	-A ${OUTPUT_DIR}/abundance.tab \
	-T 1 \
	-C ${OUTPUT_DIR}/cov_refs.gtf \
	--rf \
	-G ${REFERENCE_DIR}/Mus_musculus.GRCm38.101.chr.gtf \
	${INPUT}

# bedtools
echo "converting to fasta"
bedtools getfasta -fi ${REFERENCE_FASTA} \
	-bed ${OUTPUT_DIR}/assembly.gtf > ${OUTPUT_DIR}/assembly.fa
	
echo "DONE!"