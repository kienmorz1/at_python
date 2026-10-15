class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LL:
  def __init__(self):
    self.head = None

  def printLL(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

  def size(self):
    temp = self.head
    c = 0
    while temp is not None:
      c += 1
      temp = temp.next
    return c

  def addFirst(self,x):
    new_node = Node(x)
    new_node.next = self.head
    self.head = new_node

  def removeFirst(self):
    if self.head is None:
      return None
    temp = self.head.data
    self.head = self.head.next
    return temp

  def addLast(self,x):
    if self.head is None:
      self.addFirst(x)
    ## Step 1-> CreateNewNode
    new_node = Node(x)
    # Step 2 -> reach the last
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    # step 3 - buil a connection
    temp.next = new_node
    return

  def removeLast(self):
    if self.head is None:
      return None
    temp = self.head
    while temp is not None:
      if temp.next.next is None:
        data = temp.next.data
        temp.next = None
        return data
      temp = temp.next
    return
        


linked_list = LL()
linked_list.addFirst(5)
linked_list.addFirst(6)
linked_list.addFirst(7)
linked_list.addFirst(8)
linked_list.addFirst(9)
linked_list.printLL()
print("Removing the elements from first")
print(linked_list.removeFirst())
print(linked_list.removeFirst())
print(linked_list.removeFirst())
print("Add element in last"
)
linked_list.addLast(10)
linked_list.addLast(11)
linked_list.addLast(12)
linked_list.addLast(13)
linked_list.printLL()
print("Remove element in last"
)
print(f"Removed Last Element {linked_list.removeLast()}")
print(f"Removed Last Element {linked_list.removeLast()}")
linked_list.printLL()