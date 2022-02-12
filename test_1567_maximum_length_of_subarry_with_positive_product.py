import code_1567_maximum_length_of_subarry_with_positive_product as c

def test_example_1():
    s = c.Solution()
    assert s.getMaxLen([1,-2,-3,4]) == 4

def test_example_2():
    s = c.Solution()
    assert s.getMaxLen([0,1,-2,-3,-4]) == 3

def test_example_3():
    s = c.Solution()
    assert s.getMaxLen([-1,-2,-3,0,1]) == 2

def test_failed_104():
    s = c.Solution()
    assert s.getMaxLen([1,2,3,5,-6,4,0,10]) == 4