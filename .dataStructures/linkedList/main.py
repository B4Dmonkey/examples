class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return f"Node: <data: { self.data } next: { self.next }>"

class LinkedList:
  def __init__(self, node = None):
    self.nodes = node 

  def logList(self):
    nodes = self.nodes
    while nodes:
      print(f"elm: { nodes }")
      nodes = nodes.next

  def length(self):
    nodes = self.nodes
    count = 0
    while nodes:
      count += 1
      nodes = nodes.next
    return count

  def insert(self, node):
    node.next = self.nodes
    self.nodes = node
    

one_node = Node(1)
print(f"One node is { one_node }")
print()

empty_list = LinkedList()
print(f"Printing an empty list of length { empty_list.length() }")
empty_list.logList()
print()

linked_list = LinkedList(one_node)
linked_list.insert(Node(2))
linked_list.insert(Node(3))
print(f"Printing an list of length { linked_list.length() }")
linked_list.logList()