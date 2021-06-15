'''
Implement the unique_names method.
When passed two lists of names, it will return a list containing the names that appear in either or both lists.
The returned list should have no duplicates.

For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
should return a list containing Ava, Emma, Olivia, and Sophia in any order.
'''


#### 方法一 ####
'''
def unique_names(names1, names2):
    
     return list(set().union(names1, names2))
    
if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
'''


#### 方法二 ####
def unique_names(*names):
    r = []
    for name in names:
        r = check(name, r)
    return r

def check(n_lists, r):
    # Browse the list add append if it is not already in the list l
    for n in n_lists:
        if n not in r:
            r.append(n)
    return r

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
