# ROC-calculator-for-MOE-docking
Very basic Python 3 script computing and displaying ROC properties (curve, AOC) from MOE docking database in .txt format

This script was initially designed in the context of the "Drug Design" course at the "Faculté de Pharmacie" in Strasbourg, for a project of docking screening using MOE.

As a consequence, this script takes as input a MOE docking database training set stored in .txt format, using the "Dock" tool of MOE.

For input simplicity, the positive compounds are required to be listed first (lowest "mseq" values).
(In the context of the project, the decoys are listed at the end, which explains this choice. Indeed, I had to keep it simple for my colleagues to use it easily, and I simply didn't have time to implement a user-friendly interface... But you are welcome to contribute ! ^^)

Usage : MOE_db_ROC_analysis.py [filename.txt] ([NB_COMPOUNDS] [NB_POSITIVE_COMPOUNDS])
(By default, if NB_COMPOUNDS and NB_POSITIVE_COMPOUNDS are missing, they are set to values adapted to the project it was initially designed for)

This script computes and display : 
- the ROC (Receiver Operating Curve) curve (https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
- the AUC (Area Under Curve) associated (https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)
- the EF (Enrichment Factor) of the NB_POSITIVE_COMPOUNDS best compounds (https://dx.doi.org/10.1021%2Fjm0608356)

Warning: There is no gestion of bad input (contributors are, once again, welcomed), so please be extra careful. As a consequence, no warranty whatsoever is provided !
