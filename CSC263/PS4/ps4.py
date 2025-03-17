'''
CSC263 Winter 2025
Problem Set 4 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries

def can_visit_all_cities(numCities, dependencies):
    '''
      Pre:  numCities is the number of cities to be visited
            dependencies is a list of 2-tuples representing (city1,city2) with city1 can only be visited after city2
      Post: return whether visiting all cities is possible or not
      '''
    pass  # TODO: implement this function

if __name__ == '__main__':
    # some small test cases
    # Case 1
    numCities1: int = 25
    dependencies1 = [('reykjavik', 'stjohns'), ('limerick', 'dublin'), ('london', 'dublin'), ('brighton', 'london'),
                    ('heidelberg', 'frankfurt'),('frankfurt', 'london'), ('frankfurt', 'dublin'),
                    ('batam', 'singapore'), ('newcastle', 'sydney'),('sandiego', 'honolulu')]

    # Case 2
    numCities2: int = 10
    dependencies2 = [('paris','madrid'),('madrid','lisbon'),('lisbon','paris')]

    assert 1 == can_visit_all_cities(numCities1, dependencies1)
    assert 0 == can_visit_all_cities(numCities2, dependencies2)
