import re

str = '# p opt b3lyp/genecp scrf=(cpcm,solvent=acetonitrile) nosymm'

subedstr = re.sub('^# *(p )? *', '', str).replace('(', '').replace(')', '').replace('/', '_').replace(' ', '_')

print(subedstr)