import streamlit as st
import sympy as sp

st.title("Domain and Range Calculator")

st.write("Enter a mathematical function to find its domain and range.")

function_input = st.text_input(
    "Enter function:",
    placeholder="Example: x^2 - 2*x + 1"
)

if st.button("Calculate"):
    try:
        x = sp.symbols("x")

        # Convert ^ to ** for Python/SymPy
        expression = function_input.replace("^", "**")

        # Convert the input into a SymPy expression
        f = sp.sympify(expression)

        # Find domain
        domain = sp.calculus.util.continuous_domain(
            f, x, sp.S.Reals
        )

        # Find range
        range_value = sp.calculus.util.function_range(
            f, x, sp.S.Reals
        )

        st.success("Calculation completed!")

        st.subheader("Result")

        st.write("**Function:**")
        st.latex(f"f(x) = {sp.latex(f)}")

        st.write("**Domain:**")
        st.latex(sp.latex(domain))

        st.write("**Range:**")
        st.latex(sp.latex(range_value))

    except Exception as e:
        st.error("Please enter a valid mathematical function.")