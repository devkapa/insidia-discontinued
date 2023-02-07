import streamlit as st
import sympy as sp


def main():
    st.set_page_config(
        page_title='Scientific Calculator • Insidia', layout='wide')

    st.sidebar.title('Graphing Calculator')
    with st.sidebar:
        calculator_mode = st.radio(
            "Mode",
            ("Degrees", "Radians"),
            horizontal=True
        )

    with st.container():
        st.latex("")

    with st.container():
        scientific_1, scientific_2, scientific_3, gap, number_1, number_2, number_3, operations_1 = st.columns([2, 2, 2, 1, 1, 1, 1, 2])
        with scientific_1:
            st.button("sin(x)")
            st.button("x²")
        with scientific_2:
            st.button("cos(x)")
            st.button("xⁿ")
        with scientific_3:
            st.button("tan(x)")
            st.button("⁄")
        with gap:
            st.markdown("#")
            st.markdown("#")
            st.markdown("##")
            st.button("0")
        with number_1:
            st.button("7")
            st.button("4")
            st.button("1")
        with number_2:
            st.button("8")
            st.button("5")
            st.button("2")
        with number_3:
            st.button("9")
            st.button("6")
            st.button("3")
        with operations_1:
            st.button(r"\+")
            st.button("−")
            st.button("÷")
            st.button("×")


if __name__ == '__main__':
    main()
