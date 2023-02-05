import streamlit as st
import numpy as np
import bokeh.plotting as bk


def f(x):
    return 1 / np.cos(x)


def dy_dx(func, x):
    h = 1e-5
    return (func(x+h)-func(x))/h


def main():

    st.set_page_config(page_title='Home • Insidia', layout='wide')

    custom_css = """
                <style>
                    div.block-container {padding-top:4rem; padding-left:2.5rem;}
                </style>
                """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.markdown("# Insidia: Your partner in ~~crime~~ math.")

    example_graph(np.linspace(-100, 100, 5000), f)

    st.write("Math no longer has to be criminal. Visualise stunning live graphs, improve your understanding and check your solutions. " +
             "Get started by selecting a calculator on the sidebar.")


def example_graph(x, func):
    y = func(x)
    TOOLTIPS = [("X", "$x{0.000}"), ("Y", "$y{0.000}")]
    p = bk.figure(width=800, height=300, title="", x_range=(-10, 10), y_range=(-10, 10), tooltips=TOOLTIPS,
                  toolbar_location='right', match_aspect=True, tools='pan,hover,wheel_zoom,save,reset')
    p.line(x, y, color="navy", alpha=0.4, line_width=2)
    p.line(x, dy_dx(f, x), color="orange", alpha=0.4, line_width=2)
    p.background_fill_color = "#efefef"
    p.xaxis.fixed_location = 0
    p.yaxis.fixed_location = 0
    st.bokeh_chart(p)


if __name__ == '__main__':
    main()
