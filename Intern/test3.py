lines = int(input('line Num : '))

text = list(input() for _ in range(lines))

text[2] = text[2].split('"')
text[2] = text[2][1].split('/')
text[2][2] = text[2][2].split('.')
fileName = text[2][2][0]
print(fileName)

width, height, depth = text[3].split(':')[1].strip().split('x')
width = width.strip()
height = height.strip()
depth = depth.strip()
print(width, height, depth)

database = text[4].split('"')[1]
print(database)

text[5] = text[5].split(':')[1].strip()

objectNum = int(text[5].split()[0])
'''objectNamesTmp = text[5].split('"')
objectNamesTmp.pop(0)
objectNames = []

for i in range(len(objectNamesTmp)):
    if '}' not in objectNamesTmp[i] and objectNamesTmp[i] != ' ':
        objectNames.append(objectNamesTmp[i])

print(objectNum, objectNames)
'''

#objects = [''] * objectNum
# objectsName, xmin, ymin, xmax, ymax

for i in range(objectNum):
    objectName = text[12 + i * 7].split('"')[1]
    bounding = text[12 + i*7 + 5].split(':')[1].strip()
    print(objectName, bounding)
