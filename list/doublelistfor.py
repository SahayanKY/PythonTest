list1 = [0,1,2,3]
list2 = ['A','B','D','E']

for i,x in zip(list1,list2):
    print(i)
    print(x)

print("---------------")
for i,num in enumerate(list2):
    print(i)
    print(num)

print("---------------")


list3 = [[1.5,1.2,1.3], [1.8,1.9,2.0], [1.7,1.5,1.0], [0.5,0.7,0.3]]
for str, (x, y, z) in zip(list2,list3):
    print(str,x,y,z)