import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

st.title("Domain and Range Calculator")
st.write("Calculate the domain and range of mathematical functions.")

function_input = st.text_input(
    "Enter function:",
    placeholder="Examples: x^2, 1/x, sqrt(x), asin(x)"
)

variable_input = st.selectbox(
    "Select variable:",
    ["x", "a"]
)

st.info(
    "Use sqrt(x), log(x), sin(x), cos(x), tan(x), "
    "asin(x), acos(x), atan(x), exp(x). "
    "Use pi for π and oo for infinity."
)

if st.button("Calculate"):
    try:
        if not function_input.strip():
            st.error("Please enter a function.")
            st.stop()

        variable = sp.Symbol(variable_input)

        transformations = standard_transformations + (
            implicit_multiplication_application,
            convert_xor,
        )

        # Parse the entered mathematical expression
        f = parse_expr(
            function_input,
            local_dict={
                variable_input: variable,
                "pi": sp.pi,
                "oo": sp.oo,
            },
            transformations=transformations,
            evaluate=True,
        )

        # Reject expressions containing other free variables
        if f.free_symbols - {variable}:
            st.error(
                "Please use only the selected variable: "
                + variable_input
            )
            st.stop()

        # Find domain and range over the real numbers
        with st.spinner("Calculating domain and range..."):
            domain = sp.calculus.util.continuous_domain(
                f, variable, sp.S.Reals
            )

            range_value = sp.calculus.util.function_range(
                f, variable, sp.S.Reals
            )

        st.success("Calculation completed!")
        st.subheader("Results")

        st.write("**Function:**")
        st.latex(
            f"f({variable_input}) = {sp.latex(f)}"
        )

        st.write("**Domain:**")
        st.latex(sp.latex(domain))

        st.write("**Range:**")
        st.latex(sp.latex(range_value))

        st.caption(
            "Results are calculated symbolically by SymPy. "
            "For complicated functions, verify the result."
        )

    except NotImplementedError:
        st.warning(
            "SymPy cannot solve this function symbolically. "
            "Try a simpler expression or another form."
        )

    except Exception:
        st.error(
            "Unable to calculate this function. "
            "Check the expression and try again."
        )
