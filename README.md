## QLS rotation 1 - waldispuhl lab

### Objective:
estimate structural similarity of motifs in clusters and compare within the same cluster and between clusters

uses the __RNAalign__ algorithm from: <https://zhanggroup.org/RNA-align/> (install this)
_Sha Gong, Chengxin Zhang, Yang Zhang. RNA-align: quick and accurate alignment of RNA 3D structures based on size-independent TM-scoreRNA. (2019) Bioinformatics, 35: 4459-4461._
Ran into issues with RMalign regarding its installation on my WSL2-ubuntu but the above program worked and uses an updated TM-score.

clone this repo inside of the vernal folder
must be within the vernal environment (see environment.yml)

### File Description and Usage

___mgraph_instances.py___ contains gkm() function to extract instances from the pickled maga and meta graphs created when running vernal using: python build_motifs/main.py --meta_graph my_metagraph --do_build

___pdb_seq.py___ contains get_substructure() which (using the nx graphs) creates a cif file of the motif instance in a new directory.
This python script also contains 3 superimpose functions (rmsd) to find the structural similarity of these motif instances.
There is also intracluster_similarity() and intercluster_similarity() which hold the pipeline for running the superimposisions on a slected set of motif instances

___motif_extraction.py___ constains get_substructure()

___issue1n2.py___ fixes the following:
there are two places where the mmcif file generated by biopython is wrong:
[1] lines starting with _atom_site _should end with a space. For example,
"_atom_site.group_PDB"
should have been
"_atom_site.group_PDB "_

[2] More importantly, the atom names are wrong as shown in the following line:
ATOM 5     C 'C3'' . A A ? 1    ? -30.533  86.018  226.428 1.0 143.9  6    DA 1
According to the official mmcif format guide at
https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_atom_site.label_atom_id.html
single quotation mark (') is part of the name of the atom. In other words, C3' atoms should be written as either C3' or "C3'", but never 'C3''.

___comp_prep.py___ prepares the comparison prior to running aligner this makes the cluster directories containing the list of instances used by RNAalign

____aligner____ bash script runs the RNAalign program (combines selfer and interer)

____rnaalign_table_parser.py___ uses the outputs from the all to all comparison text files generated by the interer bash script to create bar graphs visualising the inter vs intra cluster similarity per motif instance

___parse_data.py___ has functions to find the mean similarity and to plot the QCPS from pdb_seq.py but is deprecated

___find_range.py___ selenium webscraper for the vernal website used for validation of extracted motifs (deprecated)

### Workflow
1. use line 278-280 of ___pdb_seq.py___ to set the range of the instances pulled from the metagraph
2. use ___isues1n2.py___ to fix the cif errors that biopython creates (must make changes to the script)
3. apply __comp_prep.py___ with in-script changes 
4. run ___aligner___ bash script
5. parse the data and make figures with ___rnaalign_table_parser.py___

example instance cif following edit to fix biopython cif creation issues is shown in the instance cifs subdirectory along with the folder hierarchy that the code works with in its current state (1/11/2022)

Results:
* with QCPS (advantage: same size)![8001vs8003n8103](https://user-images.githubusercontent.com/78826185/149050915-a61cd4c7-a036-41be-9e4d-49c4514abb64.png)

* with RNA-align : ![3658_RNAalign_3658to3679_6](https://user-images.githubusercontent.com/78826185/149050945-75ac601b-fab4-4477-a656-3fbc2a280924.png)
