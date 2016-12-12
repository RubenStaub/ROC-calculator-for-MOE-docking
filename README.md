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

# Troubleshooting
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

- If you have a message indicating that either "S" or "mseq" is not found, then your file is corrupted. Please check that at least "mseq" and the scoring function "S" columns are presents

- If the number of lines read is different of what you expected:

`X lines of data read` but `wc -l [input_file.txt]` is not X+1, you might have data corruption, please check your input file, especially that each line has the same number of comma-separated elements, and that there are no added line in the data part (comments, empty lines, ...)

- If you have the following message:

> Wrong number of parameters

or 

> Opening \[input_file.txt\]

> Traceback (most recent call last):

>   File "MOE_db_ROC_analysis.py", line 25, in \<module\>

>     file = open(sys.argv[1])

> FileNotFoundError: [Errno 2] No such file or directory: \[input_file.txt\]

Please refer to the usage section, and check that your file exists and that the path is correct (ensure that the script and the input file are in the same directory for greater simplicity)
