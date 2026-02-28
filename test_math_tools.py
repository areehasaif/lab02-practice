# Lab 03
# Exercise 6
# Q1
from math_tools import subtract,max_of_three,is_palindrome,find_min,remove_duplicates
def test_subtract():
    assert subtract(3,2)==1
    assert subtract(-2,-1)==-1
    assert subtract(0,0)==0
    print("test subtract: All passed")
test_subtract()

#Q3
def test_max_of_three():
    assert max_of_three(3,2,1)==3
    assert max_of_three(4,5,6)==6
    assert max_of_three(3,3,3)==3
    assert max_of_three(2,2,4)==4
    assert max_of_three(8,9,10)==10
    print("test max_of_three: All passed")
test_max_of_three()

# Q4
def test_is_palindrome():
    assert is_palindrome("aba")==True
    assert is_palindrome("tit")==True
    assert is_palindrome("s")==True
    assert is_palindrome("s a s")==True
    assert is_palindrome("ror")==True
    print("test is_palindrome: All passed")
test_is_palindrome()

# Q5
def test_find_min():
    assert find_min([1,2,3])==1
    assert find_min([2,4,5])==2
    assert find_min([3,7,8])==3
    print("test find_min: All passed")
test_find_min()

# Q6
def test_remove_duplicates():
    assert remove_duplicates([1,1,2,2,3])==[1,2,3]
    assert remove_duplicates([1,1,2,2,3,3])==[1,2,3]
    assert remove_duplicates([])==[]
    assert remove_duplicates([1,2,3,4])==[1,2,3,4]
    print("test remove_duplicates: All passed")
test_remove_duplicates()








