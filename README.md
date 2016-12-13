# ROC-calculator-for-MOE-docking
Very basic Python 3 script computing and displaying ROC properties (curve, AOC) from MOE docking database in .txt format

This Python 3 script was initially designed in the context of the "Drug Design" course at the "Faculté de Pharmacie" in Strasbourg, for a project of docking screening using MOE.

As a consequence, **this script takes as input a MOE docking database training set stored in .txt format**, using the "Dock" tool of MOE, with **comma separated values**.

For input simplicity, **the positive compounds are required to be listed first** (lowest "mseq" values).
(In the context of the project, the decoys are listed at the end, which explains this choice. Indeed, I had to keep it simple for my colleagues to use it easily, and I simply didn't have time to implement a user-friendly interface... But you are welcome to contribute ! ^^)

### Usage: python3 MOE_db_ROC_analysis.py \[input_file.txt\] \[nb_compounds\] \[nb_positive_compounds\]
(By default, if *NB_COMPOUNDS* and *NB_POSITIVE_COMPOUNDS* are missing, they are set to values adapted to the project it was initially designed for)

This script computes and display : 
- the [ROC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) (Receiver Operating Curve) curve
- the [AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve) (Area Under Curve) associated
- the [EF](https://dx.doi.org/10.1021%2Fjm0608356) (Enrichment Factor) of the *NB_POSITIVE_COMPOUNDS* best compounds and the round(*NB_POSITIVE_COMPOUNDS*/2) best compounds

In order to do so, this script use the **scoring function "S"**, and selects the best conformer (lowest "S" score) for each ligand (same "mseq" value) for plotting the ROC curve. **Note that compounds are ranked using the "S" score : the lower is "S" the more probable is the docking associated**.

#### Warning:
There is **no gestion of bad input** (contributors are, once again, welcomed), so please be extra careful. As a consequence, no warranty whatsoever is provided !

## Dependencies:
- Python 3
- [matplotlib](https://github.com/matplotlib/matplotlib).pyplot module for Python 3

# Compatibility version with Python 2.7
If you don't have Python 3 or if you have issues with Python 3 (matplotlib module for Python3 for example), I have developped a version that is compatible with Python 2.7 : **MOE_db_ROC_analysis_compatibility_mode.py**

### Usage: python MOE_db_ROC_analysis_compatibility_mode.py \[input_file.txt\] \[nb_compounds\] \[nb_positive_compounds\]

## Dependencies:
- Python >= 2.7
- [matplotlib](https://github.com/matplotlib/matplotlib).pyplot module for Python

# Data adaptation (advanced)

By default, data must be comma-separated in a table-like format, with the first line being the name of the column.
And the algorithm uses the column named "S" as scoring function.
Example:

    mol,rseq,mseq,S,rmsd_refine,E_conf,E_place,E_score1,E_refine,E_score2
    SMILES1,1,1,-8.2784767,1.592684,-68.218636,-107.6459,-11.340184,-47.245892,-8.2784767
    SMILES1,1,1,-7.8983178,1.3197823,-67.749825,-70.592857,-10.62048,-39.311447,-7.8983178
    SMILES2,1,2,-7.1144185,1.3033326,-107.42829,-77.880592,-10.105239,-40.950863,-7.1144185
    SMILES3,1,3,-8.3567276,1.732754,-36.26281,-37.163311,-8.6390247,-47.169029,-8.3567276
    SMILES3,1,3,-8.1386061,2.9906955,-40.776348,-49.089916,-9.1031685,-50.324127,-8.1386061
    SMILES3,1,3,-8.0355749,1.7808715,-40.927792,-73.855156,-9.6199598,-44.299046,-8.0355749
But you can easily change that by redefining the variables SCORE_NAME (default value 'S') and SPLIT_DELIMITER (default value ',') to fit your needs.

# Troubleshooting
- If the number of lines read is different of what you expected and/or the results are weird:

`X lines of data read` but your have have more than X+1 lines, you might have data corruption, please check your input file, especially that you don't have fused lines (it seems to be quite recurrent actually), that each line has the same number of comma-separated elements, and that there are no added line in the data part (comments, empty lines, ...)

- If you have the following message:

> Traceback (most recent call last):

>   File "MOE_db_ROC_analysis.py", line 8, in \<module\>

>     import matplotlib.pyplot.as plt

> ImportError: No module named 'matplotlib'

Install matplotlib for Python 3, or consider using the compatibility version if you have issues with the installation of this module

- If you have the following message:

> Traceback (most recent call last):

>   File "MOE_db_ROC_analysis_compatibility_mode.py", line 8, in \<module\>

>     import matplotlib.pyplot.as plt

> ImportError: No module named 'matplotlib'

Install matplotlib for Python, or you have used python3 to execute MOE_db_ROC_analysis_compatibility_mode.py (refer to usage section)

- If you have the following message:

> \_tkinter.TclError: no display name and no $DISPLAY environment variable

Python doesn't have access to your display. It is most likely that you are using Bash on Windows 10. Unfortunately, there is not much to do about it. (It would be convienient to save plot as PNG before displaying it, but I haven't implemented it, contributors are again welcomed). Consider using a real UNIX environment, or install python and matplotlib without using Bash on Windows 10.

- If you have a message indicating that either "S" or "mseq" is notin list, then your file is probably corrupted (please check that at least "mseq" and the scoring function "S" columns are presents), or your file is not comma-separated.

- If you have the following message:

> Wrong number of parameters

or 

> Opening \[input_file.txt\]

> Traceback (most recent call last):

>   File "MOE_db_ROC_analysis.py", line 25, in \<module\>

>     file = open(sys.argv[1])

> FileNotFoundError: [Errno 2] No such file or directory: \[input_file.txt\]

Please refer to the usage section, and check that your file exists and that the path is correct (ensure that the script and the input file are in the same directory for greater simplicity)
