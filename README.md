## mm_chr19_task

Task details:  from RNAseq data in BAM format generate a protein sequences database in FASTA format. <br/>
Here https://www.dropbox.com/scl/fi/c8str65tm3nnpvtd1h5o4/mouse_chr19.bam?rlkey=9730i5t2d2xl99ve5w4ty5rfi&st=ode2vbiu&dl=0

is a BAM file containing a small amount of data from a mouse RNAseq experiment. The reads have been filtered to only be from chromosome 19, which is conveniently small. Note that the strandedness of the paired reads is RF. We would like you to assemble the reads from this BAM file into transcripts, guided by the ENSEMBL v101 reference. The final output should be a FASTA file with 3-frame translations of transcripts with TPM>1. <br/>
Document your approach so your colleagues can understand and reproduce what you have done. <br/>

Reference:
[ENSEMBL v101]([https://www.ensembl.org/info/website/archives/assembly.html](http://aug2020.archive.ensembl.org/index.html))

__Workflow:__ pipeline.sh

__Steps:__
_StringTie_ - Used to make assembly guided by the _Mus_musculus.GRCm38.101.chr.gtf_ file downloaded from the above ENSEMBL v101 link. <br/>

-T argument was used to set the TPM cut off <br/>
--rf argument was used to adjust the library type <br/>
-C argument returned a coverage table with the fully covered chr19 genes <br/>
-G argument set the reference guide


