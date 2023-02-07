import random


def pre_sort(node):
    if node == None:
        return
    print(node.data, end=' ')
    pre_sort(node.left)
    pre_sort(node.right)


class tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


root = None
dataAry = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]

print('오늘 판매된 물건(중복O) -->', sellAry)

node = tree_node()
node.data = sellAry[0]
root = node

for name in sellAry[1:]:

    node = tree_node()
    node.data = name

    current = root
    while True:
        if name == current.data:
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

print("이진 탐색 트리 구성 완료!")

print('오늘 판매된 종류(중복X)--> ', end=' ')
pre_sort(root)
