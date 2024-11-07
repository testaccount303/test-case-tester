import unittest

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# Example usage
arr = [1,3,4,2,5]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)

class TestingLoopMethods(unittest.TestCase):
    
    def test_array_positive(self):
        #tests if the algorithm program works as intended
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])

    def test_array_negative(self):
        #tests if algorithm recognizes if two arrays aren't the same
        self.assertIsNot(quicksort([3, 4, 1, 2, 3]), ([1, 2, 2, 3, 4]))

    def test_array_performance(self):
        #tests if algorithm can handle a large data set
        self.assertEqual(quicksort([1,4,6,5,2,3,4,6,7,2,3,4,6,1,3,5,6,11,2,223,12,423,452,3452,346,2346,236,2346,123523,46,23465,74568,24436,45,6845,674679,34,634]), ([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 11, 12, 34, 45, 46, 223, 236, 346, 423, 452, 634, 2346, 2346, 3452, 6845, 23465, 24436, 74568, 123523, 674679]))
    
    def test_array_boundaries(self):
        #tests if algorithm can handle one item in array
        self.assertEqual(quicksort([0]), ([0]))
        #no items
        self.assertEqual(quicksort([]), ([]))
        #duplicate items
        self.assertEqual(quicksort([1,1]), ([1,1]))
        #already sorted
        self.assertEqual(quicksort([1,2,3]), ([1,2,3]))
        #reverse sorted
        self.assertEqual(quicksort([4,3,2,1]), ([1,2,3,4]))


    def test_array_idempotency(self):
        #tests if algorithm can handle multiple runs of the first test case for performance
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])
        self.assertEqual(quicksort([1,3,2,4,5]), [1,2,3,4,5])



if __name__ == '__main__':
    unittest.main()