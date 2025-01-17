## Assembly of mouse chr19 RNA-Seq data

Task details:  from RNAseq data in BAM format generate a protein sequences database in FASTA format. <br/>
Here ([Dropbox](https://www.dropbox.com/scl/fi/c8str65tm3nnpvtd1h5o4/mouse_chr19.bam?rlkey=9730i5t2d2xl99ve5w4ty5rfi&st=ode2vbiu&dl=0)) is a BAM file containing a small amount of data from a mouse RNAseq experiment. The reads have been filtered to only be from chromosome 19, which is conveniently small. Note that the strandedness of the paired reads is RF. We would like you to assemble the reads from this BAM file into transcripts, guided by the ENSEMBL v101 reference. The final output should be a FASTA file with 3-frame translations of transcripts with TPM>1. <br/>
Document your approach so your colleagues can understand and reproduce what you have done. <br/>
<br/>
Reference:
[ENSEMBL v101](http://aug2020.archive.ensembl.org/index.html)
<br/>
<br/>
To reproduce the code: <br/>
1.) Place the bam file into the bam folder <br/>
2.) The GRCm38 (v101) gtf file (see _ftp://ftp.ensembl.org/pub/release-101/gtf/mus_musculus/_) and the chr19 fasta (located in the dna folder of _ftp://ftp.ensembl.org/pub/release-101/fasta/mus_musculus/_) should be placed in the reference folder. Then run the pipeline.sh in a Linux environment where bowtie, stringtie and bedtools are available in the path. <br/>
3.) The Python script converting DNA fasta to amino acid fasta was run under Python 3.10 with the Biopython package. <br/>
<br/>
## Workflow: 
main bash script: pipeline.sh

__Steps:__  <br/>
_StringTie_ - This tool was used to make assembly guided by the _Mus_musculus.GRCm38.101.chr.gtf_ file downloaded from the above ENSEMBL v101 link. <br/>
 <br/>
-T argument was used to set the TPM cut off <br/>
--rf argument was used to adjust the library type <br/>
-C argument returned a coverage table with the fully covered chr19 genes <br/>
-G argument set the reference guide <br/>
-A turns on the returning of abundance table with gene symbols and TPM normalization <br/>
 <br/>
StringTie returns a gtf file called assembly.gtf, that is the chr19 assembly guided by the ENSEMBL v101 gtf. <br/>
 <br/>
_bedtools_ - Converting gtf file to fasta. <br/>
Using a reference fasta file bedtools getfasta command allows to convert gtf file to fasta. <br/>
 <br/>
_Translate to amino acid sequence_ - python_env/conversion.py  <br/>
conversion.py contains a biopython script converting fasta DNA sequence to fasta amino acid sequence. <br/>
The output fasta file is output/assembly_aa.fa <br/>
 <br/>
__Additional script:__  <br/>
python_env/visualization.py makes a ranked barplot in terms of TPM values using the abundance file computed by StringTie -A argument. 

__Environment:__ <br/>
The pipeline.sh was run on PDC Dardel. <br/>
Python v3.10 was used for the Biopython and visualization scripts. <br/>



