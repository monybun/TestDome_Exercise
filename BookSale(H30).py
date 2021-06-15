'''
write a method that finds n-th lowest selling book in the list.
Each element of the sales list represent a sigle sale of a book with that book's ID.
The n-th lowest selling book is the book that has more sales than n-1 books.
Assume that books sales count are unique.

For Example:
n-th lowest selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2)) should return 2.
the book with the ID=1 sold once, ID=2 sold twice,...ID=5 sold five times,
making the book with ID=1 the lowest selling book in the array and ID=2 the second lowest selling book.
'''

from collections import Counter

def nth_lowest_selling(sales, n):
    
    freq = Counter(sales)  # generate a dictionary of elements with each of their frequencies
    freq_lsit = Counter(sales).most_common()  # turning the dictionary to a list
    
    sorted_freq = sorted(freq_lsit, key = lambda x:x[1])
    n_thlowest = sorted_freq[n-1][0]
    
    return n_thlowest

if __name__ == "__main__":
    print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))
