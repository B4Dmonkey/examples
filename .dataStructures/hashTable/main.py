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

  def insert(self, node):
    node.next = self.nodes
    self.nodes = node


class HashTable:
  def __init__(self, node):
    self.table = LinkedList()
  
  def hash():
    pass

  def insert(val):
    pass