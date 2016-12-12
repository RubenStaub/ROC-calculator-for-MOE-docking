# ROC curve/AOC calculator using MOE database input file (in .txt format)
# Active compoounds must be placed first (lowest mseq values)
# Usage : MOE_db_ROC_analysis.py [filename.txt] ([NB_COMPOUNDS] [NB_POSITIVE_COMPOUNDS])
# If not given, NB_COMPOUND = 100 and NB_POSITIVE_COMPOUNDS = 10
# For more information, contact Ruben Staub: ruben [dot] staub [at-sign] etu [dot] unistra [dot] fr

import sys
import matplotlib.pyplot as plt

if(len(sys.argv) != 2 and len(sys.argv) != 4):
	print('Wrong number of parameters\n')
	print('ROC curve/AUC calculator using MOE database input file (in .txt format)\nActive compoounds must be placed first (lowest mseq values)\nUsage : MOE_db_ROC_analysis.py [filename.txt] ([NB_COMPOUNDS] [NB_POSITIVE_COMPOUNDS])\nIf not given, NB_COMPOUND = 100 and NB_POSITIVE_COMPOUNDS = 10\nFor more information, contact: ruben [dot] staub [at-sign] etu [dot] unistra [dot] fr')
	exit()

MAX_VALUE = 65536
if(len(sys.argv) == 4):
        NB_COMPOUNDS = sys.argv[2]
        NB_POSITIVE = sys.argv[3]
else:
	NB_COMPOUNDS = 100
	NB_POSITIVE = 10
NB_EF_TEST = NB_POSITIVE

print('Opening '+sys.argv[1])
file = open(sys.argv[1])

scores = [MAX_VALUE for i in range(NB_COMPOUNDS)]
line = file.readline().split('\n')[0]
cols = line.split(',')
nb_cols = len(cols)
score_col = cols.index('S')
mseq_col = cols.index('mseq')

line_count = 0
for line in file.readlines():
	data = line.split('\n')[0].split(',')
	if(len(data) != nb_cols):
		break
	score = float(data[score_col])
	mseq = int(data[mseq_col])
	if(score < scores[mseq-1]):
		scores[mseq-1]=score
	line_count += 1

file.close()
print('{:d} lines of data read'.format(line_count))

tp = [0 for i in range(100)]
fp = [0 for i in range(100)]

extract_score = sorted(scores)
for nb in range(100):
	for score in extract_score[0:nb]:
		if(scores.index(score) < 10):
			tp[nb] += 1
		else:
			fp[nb] += 1

tpr = [tp[i]/NB_POSITIVE for i in range(len(tp))]
fpr = [fp[i]/(NB_COMPOUNDS-NB_POSITIVE) for i in range(len(fp))]
print('Data extracted')

auc = 0
for i in range(1,len(tpr)):
	auc += (fpr[i]-fpr[i-1])*(tpr[i]+tpr[i-1])/2
print('AUC computed: {:.3f}'.format(auc))

ef = (tp[NB_EF_TEST-1]/NB_EF_TEST)/(NB_POSITIVE/NB_COMPOUNDS)
ef_half = (tp[round(NB_EF_TEST/2)-1]/NB_EF_TEST)/(NB_POSITIVE/NB_COMPOUNDS)
print('EF{:d} computed: {:.2f}'.format(NB_EF_TEST,ef))
print('EF{:d} computed: {:.2f}'.format(round(NB_EF_TEST/2),ef_half))

print('Displaying ROC curve')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve (AUC = {:.2f}, EF{:d} = {:.2f}, EF{:d} = {:.2f})'.format(auc,NB_EF_TEST,ef,round(NB_EF_TEST/2),ef_half))
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1],color='black')
plt.show()

print('Exiting')
exit()

#    Copyright (C) 2016  STAUB Ruben

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/gpl.html>.
