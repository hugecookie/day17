import os


class tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


root = None
nameAry = []


folderName = 'C:/Program Files/Common Files/'
for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        nameAry.append(fname)

node = tree_node()
node.data = nameAry[0]
root = node

dupNameAry = []

for name in nameAry[1:]:

    node = tree_node()
    node.data = name

    current = root
    while True:
        if name == current.data:
            dupNameAry.append(name)
            break
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

dupNameAry = list(set(dupNameAry))

print(f'{folderName} 및 그 하위 디렉터리의 중복된 파일 목록 -->')
print(dupNameAry)
