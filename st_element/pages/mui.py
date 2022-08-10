import streamlit as st
import streamlit_elements as ste

st.set_page_config(layout="wide")
st.title("MUI")
st.write("material-ui: https://mui.com/material-ui/react-backdrop/")
st.write("-"*5)


def nivo_graph():
    products = "Products"
    el_type01 = "商品A"
    el_type02 = "商品B"
    el_type03 = "商品C"

    DATA = [
        { products: "耐火性能", el_type01: 100, el_type02: 41, el_type03: 61 },
        { products: "防水性能", el_type01: 91, el_type02: 37, el_type03: 72 },
        { products: "耐久年数", el_type01: 75, el_type02: 28, el_type03: 56 },
        { products: "故障率", el_type01: 64, el_type02: 90, el_type03: 30 },
        { products: "平均満足度", el_type01: 78, el_type02: 25, el_type03: 99 },
    ]

    nn = ste.nivo.Radar(
        data=DATA,
        keys=[ el_type01, el_type02, el_type03 ],
        indexBy=products,
        valueFormat=">-.2f",
        margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
        borderColor={ "from": "color" },
        gridLabelOffset=36,
        dotSize=10,
        dotColor={ "theme": "background" },
        dotBorderWidth=2,
        motionConfig="wobbly",
        legends=[
            {
                "anchor": "top-left",
                "direction": "column",
                "translateX": -50,
                "translateY": -40,
                "itemWidth": 80,
                "itemHeight": 20,
                "itemTextColor": "#999",
                "symbolSize": 12,
                "symbolShape": "circle",
                "effects": [
                    {
                        "on": "hover",
                        "style": {
                            "itemTextColor": "#000"
                        }
                    }
                ]
            }
        ],
        theme={
            "background": "#FFFFFF",
            "textColor": "#31333F",
            "tooltip": {
                "container": {
                    "background": "#FFFFFF",
                    "color": "#31333F",
                }
            }
        }
    )
    return nn



with ste.elements("dashboard"):
    ste.mui.Alert("React mui", severity="success")

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        ste.dashboard.Item("first_item", 0, 0, 6, 3),
        ste.dashboard.Item("second_item", 6, 0, 6, 2,),
        ste.dashboard.Item("third_item", 8, 2, 4, 2, ),
        ste.dashboard.Item("force_item", 0, 4, 4, 1, ),
        ste.dashboard.Item("fifth_item", 0, 5, 8, 2, ),
        # dashboard.Item("force_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        # dashboard.Item("fifth_item", 0, 2, 1, 1, isResizable=False),
    ]


    with ste.dashboard.Grid(layout):
        ste.mui.Paper(nivo_graph(), key="first_item")
        ste.mui.Paper(
            ste.mui.Box(
                "React mui を利用して生成しているページです",
                sx={
                    # "bgcolor": "background.paper",
                    "font-size": "18px",
                    "font-weight": 800,
                    "bgcolor": "#226622",
                    "boxShadow": 10,
                    "borderRadius": 2,
                    "p": 3,
                    "minWidth": 300,
                    "margin": "5px 5px 0 5px",
                },
                elevation=24
            ),
            ste.mui.Box("margin:20px",sx={"color":"#FFFFFF","bgcolor":"#111111", "padding":"30px", "margin":"20px"}),
            ste.mui.Box(
                ste.mui.TextField(
                    label="Save Dash Bords",
                    defaultValue="Type here",
                    variant="outlined",
                    sx={"margin":"5px"},
                ),
                ste.mui.TextField(
                    label="Project Name",
                    defaultValue="Type here",
                    variant="outlined",
                    sx={"margin":"5px"},
                ),
            ),
            key="second_item", elevation=3, variant="outlined", square=True
        )
        ste.mui.Paper(
            ste.mui.TextField(label="Please Input Something", sx={"margin": "20px"}),
            ste.mui.Button(
                ste.mui.icon.EmojiPeople,
                ste.mui.icon.DoubleArrow,
                "Button with multiple children",
                sx={"margin": "20px"}
            ),
            key="third_item",
        )
        ste.mui.Paper(
            ste.mui.SpeedDial(ariaLabel="tt", sx={"position":"absolute", "bottom":12, "right":12}, icon=ste.mui.icon.ClearSharp),
            ste.mui.Pagination(count={20}, color="secondary", sx={"position":"absolute", "top":12, "left":12}),
            key="force_item",
        )

        ste.mui.Paper(
            ste.mui.Skeleton(variant="text"),
            ste.mui.Skeleton(variant="circular"),

            ste.mui.ButtonGroup(
                ste.mui.Button("車いす", ste.mui.icon.AccessibleForwardRounded),
                ste.mui.Button("", ste.mui.icon.Build, sx={"bgcolor": "orange"}),
                ste.mui.Button("Three"),
                variant="outlined",
                sx={
                    "width": "600px",
                    "margin-left": "33.3%",
                }
            ),
            sx={"bgcolor": "#6f88f6"},
            key="fifth_item"
        )