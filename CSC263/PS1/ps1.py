'''
CSC263 Winter 2025
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

class Heap:
  '''
  initializes a min/max heap depending on the value of minimum
  A heap is an almost complete binary tree with the property that every node is either
  greater or less than its children
  '''
  def __init__(self, minimum: bool):
    self.min = 2 * int(not minimum) - 1
    self.lst = []
    self.size = 0

  '''
  Inserts x into the heap 
  '''
  def insert(self, x: int):
    self.lst.append(x)
    self.size += 1

    # insert new element
    i = len(self.lst) - 1
    while i > 0:
      if(self.min * self.lst[i] <= self.min * self.lst[(i - 1) // 2]):
        break
      self.lst[(i - 1) // 2], self.lst[i] = self.lst[i], self.lst[(i - 1) // 2]
      i = (i - 1) // 2
    pass

  '''
  Removes the root from the heap
  '''
  def remove(self) -> int:
    i = 0
    self.lst[0], self.lst[-1] = self.lst[-1], self.lst[0]
    x = self.lst.pop()
    self.size -= 1

    while 2 * i + 1 < len(self.lst):
      if 2 * i + 2 >= len(self.lst) or self.min * self.lst[2 * i + 1] >= self.min * self.lst[2 * i + 2]:
        self.lst[i], self.lst[2 * i + 1] = self.lst[2 * i + 1], self.lst[i] # swap with left child
        i = i * 2 + 1
      else:
        self.lst[i], self.lst[2 * i + 2] = self.lst[2 * i + 2], self.lst[i] # swap with right child
        i = i * 2 + 2
    return x

  def get_size(self) -> int:
    return self.size

  def peek(self) -> int:
    return self.lst[0]

def spy263(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of find_spy results
  '''
  spy_position = 0
  size = 0
  spy_heap = Heap(minimum=False)
  other_heap = Heap(minimum=True)
  spies = []
  for command in commands:
    if(command == 'find_spy'):
      spies.append(spy_heap.peek())
    else:
      val = int(command.split(' ')[1])
      size += 1
      new_spy_position = -(-size * 263 // 1000)
      if new_spy_position != spy_position:
        if other_heap.get_size() == 0 or val <= other_heap.peek():
          spy_heap.insert(val)
        else:
          other_heap.insert(val)
          spy_heap.insert(other_heap.remove())
      else:
        if spy_heap.get_size() == 0 or val < spy_heap.peek():
          other_heap.insert(spy_heap.remove())
          spy_heap.insert(val)
        else:
          other_heap.insert(val)
      spy_position = new_spy_position
  return spies # TODO: implement this function

# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == '__main__':
  # some small test cases
  # Case 1
  assert [15, 6, 2] == spy263(
      ['insert 15',
       'find_spy',
       'insert 6',
       'insert 2',
       'insert 8',
       'find_spy',
       'insert -5',
       'insert -8',
       'insert 3',
       'insert 20',
       'find_spy',
      ])

