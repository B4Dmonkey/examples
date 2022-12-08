class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node

class Entry:
  def __init__(self,key, value):
    self.key = key
    self.value = value

class HashTable:
  def __init__(self):
    self.table = LinkedList()

  def insert(self, value: list):
    key = set(value)
    if not self.search(key):
      self.table.insert(Entry(key, value))

  def search(self, key: set):
    table = self.table
    while table and table.data.key != key:
      table = table.next
    return table
  
  def toList(self):
    res = []
    table = self.table

    while table:
      res.append(table.data.value)
      table = table.next

    return res

def threeSums(nums: list ):
  res = HashTable()
  for i in nums:
    for k in nums[1:]:
      for j in nums[2:]:
        if (0 == (i + k + j)):
          res.insert([i,k,j])
  return res.toList()