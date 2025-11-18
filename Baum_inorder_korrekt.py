arr = [35, 17, 88, 93, 91, 12, 8, 47, 58, 32, 1, 69, 62, 74, 99, 23, 18, 11]

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def einfuegen(node, data):
    if node is None:
        return Node(data)

    if data < node.data:
        node.left = einfuegen(node.left, data)
    elif data > node.data:
        node.right = einfuegen(node.right, data)
    
    return node

def erstelleBaum(arr):
    wurzel = Node(arr[0]) #Erstelle ein Objekt namens "wurzel" der Klasse Node()

    for i in range(1, len(arr)):
        einfuegen(wurzel, arr[i])
    
    return wurzel


def ausgabeInorder(node):
    if node is not None:
        ausgabeInorder(node.left)
        print(node.data, end=" ")
        ausgabeInorder(node.right)

def ausgabePreorder(node):
    if node is not None:
        print(node.data, end=" ")
        ausgabePreorder(node.left)
        ausgabePreorder(node.right)

baum = erstelleBaum(arr)

print("\nInorder:")
ausgabeInorder(baum)
print("\nPreorder:")
ausgabePreorder(baum)

