import sympy as sp

x = sp.symbols('x')

print("===================================")
print("     DOMAIN AND RANGE CALCULATOR")
print("===================================")

function_input = input("Enter a function of x: ")

try:
    # Convert ^ into ** so users can enter x^2
    function_input = function_input.replace("^", "**")

    # Convert input into a SymPy expression
    function = sp.sympify(function_input)

    # Calculate Domain
    domain = sp.calculus.util.continuous_domain(
        function, x, sp.S.Reals
    )

    # Calculate Range
    range_value = sp.calculus.util.function_range(
        function, x, sp.S.Reals
    )

    print("\nFunction:", function)
    print("Domain :", domain)
    print("Range  :", range_value)

except Exception:
    print("\nInvalid function!")
    print("Please enter a valid function.")