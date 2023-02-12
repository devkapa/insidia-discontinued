import streamlit as st
import sympy as sp


class Formula:

    formula_str: str
    point_at: int

    def __init__(self) -> None:
        self.formula_str = ''
        self.point_at = -1

    def __repr__(self) -> str:
        modified_str = list(self.formula_str)
        modified_str.insert(self.point_at + 1, "❚")
        return "".join(modified_str)

    def add(self, expression) -> None:
        modified_str = list(self.formula_str)
        modified_str.insert(self.point_at + 1, expression)
        self.formula_str = "".join(modified_str)
        if not "{}" in expression:
            self.point_at += len(list(expression))
            return
        self.point_at += len(list(expression)) - 1

    def move_right(self) -> None:
        if not self.point_at > len(list(self.formula_str)) - 1:
            if list(self.formula_str)[self.point_at+1] == "^":
                self.point_at += 2
                return
            if list(self.formula_str)[self.point_at+1] == "\\":
                for index, char in enumerate(list(self.formula_str)[self.point_at+1:]):
                    if char == "{":
                        self.point_at = (
                            index+1) + len(list(self.formula_str)[:self.point_at])
                        return
            self.point_at += 1

    def move_left(self) -> None:
        if not self.point_at < 0:
            if list(self.formula_str)[self.point_at] == "{":
                for index, char in enumerate(list(self.formula_str)[:self.point_at]):
                    if index < 7:
                        if char == "\\":
                            self.point_at = index-1
                    else:
                        self.point_at -= 2
                        break
                return
            self.point_at -= 1

    def get_formula(self) -> None:
        return self.formula_str

    def evaluate(self) -> None:  # Change return type later
        answer = '1^{2}'
        return answer

    def clear(self) -> None:
        self.formula_str = ''
        self.point_at = -1


def main():
    st.set_page_config(
        page_title='Scientific Calculator • Insidia', layout='wide')

    st.sidebar.title('Scientific Calculator')
    with st.sidebar:
        calculator_mode = st.radio(
            "Mode",
            ("Degrees", "Radians"),
            horizontal=True
        )

    if 'current_formula' not in st.session_state:
        st.session_state['current_formula'] = Formula()

    current_formula = st.session_state['current_formula']

    formula_display = st.container()

    with st.container():
        st.markdown("# ")

    with st.container():
        scientific_1, scientific_2, scientific_3, gap, number_1, number_2, number_3, operations_1 = st.columns([
            2, 2, 2, 1, 1, 1, 1, 2])
        with scientific_1:
            sinx = st.button("sin(x)")
            xpower2 = st.button("x²")
            left_parenthesis = st.button("(")
        with scientific_2:
            cosx = st.button("cos(x)")
            xpowern = st.button("xⁿ")
            right_parenthesis = st.button(")")
        with scientific_3:
            tanx = st.button("tan(x)")
            fraction = st.button(" ⁄ ")
            root = st.button("√")
        with gap:
            st.markdown("#")
            st.markdown("#")
            st.markdown("##")
            zero = st.button("0")
        with number_1:
            seven = st.button("7")
            four = st.button("4")
            one = st.button("1")
        with number_2:
            eight = st.button("8")
            five = st.button("5")
            two = st.button("2")
        with number_3:
            nine = st.button("9")
            six = st.button("6")
            three = st.button("3")
        with operations_1:
            plus = st.button(r"\+")
            minus = st.button("−")
            divide = st.button("÷")
            multiply = st.button("×")

        space_1, content_section, space_2 = st.columns([1.3, 1, 1])

        with space_1:
            left = st.button("←")
            right = st.button("→")

        with content_section:
            clear = st.button("Clear")

        if left:
            current_formula.move_left()

        if right:
            current_formula.move_right()

        if clear:
            current_formula.clear()

        if root:
            current_formula.add(r"\sqrt{}")

        if sinx:
            current_formula.add("sin(")

        if cosx:
            current_formula.add("cos(")

        if tanx:
            current_formula.add("tan(")

        if left_parenthesis:
            current_formula.add(r"(")

        if right_parenthesis:
            current_formula.add(r")")

        if zero:
            current_formula.add("0")

        if one:
            current_formula.add("1")

        if two:
            current_formula.add("2")

        if three:
            current_formula.add("3")

        if four:
            current_formula.add("4")

        if five:
            current_formula.add("5")

        if six:
            current_formula.add("6")

        if seven:
            current_formula.add("7")

        if eight:
            current_formula.add("8")

        if nine:
            current_formula.add("9")

        if plus:
            current_formula.add("+")

        if minus:
            current_formula.add("-")

        if divide:
            current_formula.add("/")

        if multiply:
            current_formula.add("*")

        if xpower2:
            current_formula.add(r"^{2}")

        if xpowern:
            current_formula.add(r"^{}")

    with formula_display:
        if current_formula.get_formula() != "":
            st.latex(str(current_formula))
        else:
            st.latex("❚")

    st.session_state['current_formula'] = current_formula


if __name__ == '__main__':
    main()
