#!/bin.bash --login
#PBS -l walltime=01:00:00
#PBS -l select=1:ncpus=8
#PBS -N 2018_join_paired_ends
#PBS -a d411-training
cd $PBS_O_WORKDIR
module load miniconda/python2
source activate qiime1
export TMPDIR=~/qiime_tmp
#joining paired ends
echo "joining paired ends via Seqprep"
time join_paired_ends.py -m Seqprep -f Read1.fastq.gz -r Read2.fastq.gz -b Index.fastq.gz -o Seqprep_joined
source deactivate
