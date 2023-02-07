class treenode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


node1 = treenode()
node1.data = '피카츄'

node2 = treenode()
node2.data = '라이츄'
node1.left = node2

node3 = treenode()
node3.data = '꼬부기'
node1.right = node3

node4 = treenode()
node4.data = '어니부기'
node2.left = node4

node5 = treenode()
node5.data = '거북왕'
node2.right = node5

node6 = treenode()
node6.data = '파이리'
node5.right = node6

node7 = treenode()
node7.data = '또가스'
node3.right = node7


def presort(node):
    if node is None:
        return
    print(node.data, end='->')
    presort(node.left)
    presort(node.right)


def insort(node):
    if node is None:
        return
    insort(node.left)
    print(node.data, end='->')
    insort(node.right)


def postsort(node):
    if node is None:
        return
    postsort(node.left)
    postsort(node.right)
    print(node.data, end='->')


print('전위 순회 : ', end='')
presort(node1)
print('끝')

print('중위 순회 : ', end='')
insort(node1)
print('끝')

print('후위 순회 : ', end='')
postsort(node1)
print('끝')
