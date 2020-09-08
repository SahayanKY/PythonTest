lineStrList = []

lineStrList.append('hoge')
lineStrList.append('huga')

str = '\n'.join(lineStrList)

lineStrList2 = []

lineStrList2.append('hello')
lineStrList2.append(str)
lineStrList2.append('bye')

str = '\n'.join(lineStrList2)
print(str)