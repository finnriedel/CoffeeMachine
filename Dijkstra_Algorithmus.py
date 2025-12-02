class Node:
 def __init__(self, data):
    self.data = data
    self.next = None


koblenz = Node(0)


koblenz.next = pruem = Node(111)
koblenz.next = bielstein = Node(114)
pruem.next = moenchengladbach = Node(143)
pruem.next = bergischgladbach = Node(125)
bielstein.next = olpe = Node(33)
bielstein.next = bergischgladbach = Node(33)
bielstein.next = moenchengladbach = Node(106)
olpe.next = bergischgladbach = Node(64)
moenchengladbach.next = leverkusen = Node(83)
bergischgladbach.next = leverkusen = Node(24)

def dijkstra(start):
  aktuellerknoten = start
  while aktuellerknoten.next != 0:
    
    print(aktuellerknoten.data, end ="km|")
    aktuellerknoten = aktuellerknoten.next




dijkstra(koblenz)
  





