arr = [35, 17, 88, 93, 91, 12, 8, 47, 58, 32, 1, 69, 62, 74, 99, 23, 18, 11]


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def fuelleBaum(arr):

    wurzel = Node(arr[0])
    queue = [wurzel]

    i = 1
    n = len(arr)

    while i < n:
        parent = queue.pop(0)

        if i < n:
            links = arr[i]
            if links != 0:
                left_node = Node(links)
                parent.left = left_node
                queue.append(left_node)
            i += 1
        
        if i < n:
            rechts = arr[i]
            if rechts != 0:
                right_node = Node(rechts)
                parent.right = right_node
                queue.append(right_node)
            i += 1
            
    return wurzel


baum = fuelleBaum(arr)

def ausgabeInorder(node):
    if node:
        ausgabeInorder(node.left)
        print(node.data, end=" ")
        ausgabeInorder(node.right)
 
def ausgabePreorder(node):
    if node:
        print(node.data, end=" ")
        ausgabePreorder(node.left)
        ausgabePreorder(node.right)


print("Inorder:")
ausgabeInorder(baum)
print("\nPreorder")
ausgabePreorder(baum)