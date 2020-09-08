import re

gjfFileName = '/home/yuki/hoge/methane.gjf'
chkFileName = re.sub('.gjf$', '.chk', re.sub('.*/', '', gjfFileName))
print(chkFileName)