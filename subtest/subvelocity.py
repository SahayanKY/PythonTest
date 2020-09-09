import re
import time

str = "#p opt b3lyp/genecp scrf=(cpcm,solvent=acetonitrile) nosymm"

start = time.time()
for i in range(10000):
    #10000回繰り返し
    #0.11093
    #0.08494
    #0.05896
    #0.10293
    #0.07495
    #0.07795
    #0.07995
    #0.08394
    #0.09594
    #0.09594
    #実行時間0.086(15) s (n=10)
    #subedstr = re.sub('[()#]', '', re.sub('[/ ]', '_', str))


    #10000回繰り返し
    #0.015989
    #0.028980
    #0.025983
    #0.019988
    #0.030979
    #0.017988
    #0.016989
    #0.017986
    #0.024984
    #0.021986
    #実行時間0.022(5) s (n=10)
    subedstr = str.replace('(', '').replace(')', '').replace('#', '').replace('/', '_').replace(' ', '_')


end = time.time()
print(end-start)