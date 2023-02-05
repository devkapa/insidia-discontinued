import streamlit as st
from bokeh.plotting import figure


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

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')

    p.line(x, y, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)


if __name__ == '__main__':
    main()
