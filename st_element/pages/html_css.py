import streamlit as st
import streamlit_elements as ste

st.set_page_config(layout="centered")
st.title("html")
st.write("css-style: https://emotion.sh/docs/object-styles")
st.write("-"*5)
st.subheader("・Contents")

with st.sidebar:
    st.subheader("ButtonRayout")
    before_text = st.text_input("before_text", value="(*'▽')")
    after_text = st.text_input("after_text", value="(# ﾟДﾟ)")
    btn_h = st.slider("Button-Heigh (px)", min_value=10, max_value=100, value=50)
    btn_w = st.slider("Button-Width (px)", min_value=100, max_value=680, value=400)

if "first_name" not in st.session_state:
    st.session_state.first_name = "Elm01"

class ButtonCss():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def outer(self):
        return { 
            "position": "relative",
            "display": "inline-block",
            "transform-style": "preserve-3d",
            "perspective": "2000px",
            "width": f"{self.width}px",
            "height": f"{self.height}px",
            "margin": "0 auto",
            "cursor": "pointer",
            "transition": "all 0.3s",
            # "transform-origin": f"center center {self.height* 0.5 * -1}px",
            "transform-origin": f"50% 50%",
            "&:hover": {
                "transform": "rotateX(270deg)",
            },
        }

    def inner(self):
        return {
            "position": "absolute",
            "top": 0,
            "left": 0,
            "width": "100%",
            "height": "100%",
            "border": "1px solid red",
            "border-radius": "10px",
            "line-height": f"{self.height-2}px",
            "text-align": "center",
            "font-weight": "900",
        }

    def before(self):
        inner_css = self.inner()
        add_css = {
            "background-color": "white",
            "color": "black",
            "transform": "rotateX(0deg)",
        }
        return {**inner_css, **add_css}

    def after(self):
        inner_css = self.inner()
        add_css = {
            "background-color": "black",
            "color": "white",
            "transform": f"rotateX(-270deg)",
        }
        return {**inner_css, **add_css}


btn_css = ButtonCss(btn_h, btn_w)

with ste.elements("HTML_Elements"):

    ste.html.a(
        ste.html.span(
            before_text,
            css=btn_css.before()
        ),
        ste.html.span(
            after_text,
            css=btn_css.after(),
        ),
        css=btn_css.outer()
    )

    ste.html.div(
        "div component",
        css={
            "height": "200px",
            "background": ['red','linear-gradient(#e66465, #9198e5)'],
            "borderRadius": "20%",
            "top": "150px",
            "left": "150px",
            "margin": "20px auto"
        },
    )
    ste.html.div(
        "Second Component",
        css={
            "width": "350px",
            "margin-left": "auto",
            "margin-right": "auto",
            "marginTop": "50px",
            "height": "100px",
            "backgroundColor": "#EEEEEE",
            "borderRadius": "50%",
            "top": "50px",
            "left": "50px",
            "textAlign": "center",
            "color": "hotpink"
        }
    )
