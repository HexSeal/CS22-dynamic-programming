class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(rows):
        for col in range(cols):
            dp_table[row][col] == float('inf')

    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    # print(items, capacity)
    if len(items) == 0 or capacity <= 0:
        return 0
    
    # Take the value of the first item, add that to whatever the value of the remaining items would be, but with less capacity
    value_with = items[0][2] + knapsack(items[1:], capacity - items[0][1])
    
    # Assuming the first item doesn't go in the knapsack, what would the value be
    value_without = knapsack(items[1:], capacity)
    
    if capacity - items[0][1] < 0:
        return value_without
    else:
        return max(value_with, value_without)

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    # Go through the table
    for row in range(rows):
        for col in range(cols):
            # If either the rows or the column go past the edge of the table, go back
            if rows == 0 or cols == 0:
                dp_table[row][col] = 0
            
            # If it's over capacity go back
            elif items[row-1][1] > col:
                dp_table[row][col] = dp_table[row-1][col]
                
            else:
                value_with = items[row-1][2] + dp_table[row-1][col - items[row-1][1]]
                value_without = dp_table[row-1][col]
                dp_table[row][col] = max(value_with, value_without)

    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    # Base Case:
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Other base case
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    
    option1 = edit_distance(str1[:-1], str2)
    option2 = edit_distance(str1, str2[:-1])
    option3 = edit_distance(str1[:-1], str2[:-1])
    
    return min(option1, option2, option3) + 1

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                dp_table[row][col] = max(row, col)
                
            elif str1[row-1] == str2[col-1]:
                dp_table[row][col] = dp_table[row-1][col-1]
                
            else:
                insert = dp_table[row-1][col]
                delete = dp_table[row][col-1]
                replace = dp_table[row-1][col-1]
                
                dp_table[row][col] = min(insert, delete, replace) + 1

    print(dp_table)
    return dp_table[-1][-1]

