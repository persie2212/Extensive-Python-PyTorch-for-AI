#Session 3

#Qualean Class

Qualean class is inspired by Boolean+Quantum concepts. We assigned it only 3 possible real states. 
True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. We assigned it a 
real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and 
stores that number internally after using Bankers rounding to 10th decimal place.

# __init__
To get called by the __new__ method.

# __and__
To get called AND with assignment e.g. a and b.

# __or__
To get called OR with assignment e.g. a or b.

# __repr__
To get called by built-int repr() method to return a machine readable representation of a type.

# __str__
To get called by built-int str() method to return a string representation of a type.

# __add__
To get called on add operation using + operator

# __eq__
To get called comparator operator with assignment e.g. a == b.


# __float__
To get called by built-int float() method to convert a type to float.

# __ge__
method is added in the Qualean class to overload the >= operator.

#  __gt__
method is added in the Qualean class to overload the > operator.

# __invertsign__
To get called for inversion operator.

# __le__
To get called on comparison using <= operator.

# __lt__
To get called on comparison using < operator.

# __mul__
To get called on multiplication using * operator.

# __sqrt__
To get square root AND with assignment e.g. a.__sqrt().

# __bool__
If an object defines the __bool__ method, then Python calls that method to determine its truth value.

['__and__', '__or__', '__repr__', '__str__', '__add__',
'__eq__', '__float__', '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__',
 '__mul__', '__sqrt__', '__bool__'