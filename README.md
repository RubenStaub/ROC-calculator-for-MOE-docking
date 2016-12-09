# ROC-calculator-for-MOE-docking
Very basic Python 3 script computing and displaying ROC properties (curve, AOC) from MOE docking database in .txt format

This Python 3 script was initially designed in the context of the "Drug Design" course at the "Faculté de Pharmacie" in Strasbourg, for a project of docking screening using MOE.

As a consequence, **this script takes as input a MOE docking database training set stored in .txt format**, using the "Dock" tool of MOE.

For input simplicity, **the positive compounds are required to be listed first** (lowest "mseq" values).
(In the context of the project, the decoys are listed at the end, which explains this choice. Indeed, I had to keep it simple for my colleagues to use it easily, and I simply didn't have time to implement a user-friendly interface... But you are welcome to contribute ! ^^)

### Usage: MOE_db_ROC_analysis.py \[input_file.txt\] \[nb_compounds\] \[nb_positive_compounds\]
(By default, if nb_compounds and nb_positive_compounds are missing, they are set to values adapted to the project it was initially designed for)

This script computes and display : 
- the [ROC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) (Receiver Operating Curve) curve
- the [AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve) (Area Under Curve) associated
- the [EF](https://dx.doi.org/10.1021%2Fjm0608356) (Enrichment Factor) of the NB_POSITIVE_COMPOUNDS best compounds

#### Warning:
There is **no gestion of bad input** (contributors are, once again, welcomed), so please be extra careful. As a consequence, no warranty whatsoever is provided !
