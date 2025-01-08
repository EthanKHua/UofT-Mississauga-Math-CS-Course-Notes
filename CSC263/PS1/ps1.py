'''
CSC263 Winter 2025
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def spy263(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of find_spy results
  '''
  pass # TODO: implement this function

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

