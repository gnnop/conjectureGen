from sympy import *
from theory_substrate_generator import *
from equation_generator import *

"""
This is a continuously run program.
It should save it state when I terminate it.


"""

#Future equation.
#n is the tree complexity, k is the symbol number, a is index
def grab_equation(n, k, a):
    return 0
"""
After applying this, we should simplify it and hash
the string to give a simple equation. After acquiring
a list of hashed equations of a certain number of 
symbols, we begin the theory injection.




Following the theory injection, we generate a substrate to
test on, up to 3000 graphs. Following this, we print
successful, non-trivial theories to both the console
and append them to a txt file.



Eventually, I want to accumulate a list of known graph
theorems. What should happend then, is if we have a known
list of equations, we can try to test the theory in terms
of the equations by treating equation context as free
and testing for free variables, which receive arbitrary
data injections. Since this is very fast, we test a 
million numbers, and if they all match, we decide that
the generated eqation is algebraically dependent on
known equations ad therefore uninteresting. Else,
we have something depedent on a deep structure,
so I list it.

This effectively makes a completely non-interactive
algorith that will list me equatons for an arbitrary
theory and find internall connections
"""

init_printing()

# Define the symbols used in the expression
x, y, z = symbols('x y z')

# Define an arbitrary expression to simplify
expr = x**2 + 2*x*y + y**2 + 2*x*z + 2*y*z + z**2

# Simplify the expression
simplified_expr = simplify(expr)

# Print the original and simplified expressions
print("Original expression:", expr)
print("Simplified expression:", simplified_expr)


from sympy import *
init_printing()

# Define the symbols used in the expressions
x, y = symbols('x y')

# Define the two expressions to add together
expr1 = x**2 + 2*x*y + y**2
expr2 = x**2 - 2*x*y + y**2

# Add the expressions together
combined_expr = simplify(expr1 + expr2)

# Print the original expressions and the combined expression
print("Expression 1:", expr1)
print("Expression 2:", expr2)
print("Combined expression:", combined_expr)
