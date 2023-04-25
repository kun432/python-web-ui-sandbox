import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import JsCode

st.set_page_config(
    layout="wide",
)

df = pd.read_html("https://db.netkeiba.com/race/201902010101")[0]

# dfの列名から空白を除く
df.columns = df.columns.str.replace(" ", "")


st.subheader("通常の表示")
df

st.subheader("st.dataframeと使った場合")
st.dataframe(df)

st.subheader("AgGridを使った場合")

st.text("streamlitテーマ（デフォルト）")
AgGrid(df)  # theme="streamlit"

st.text("alpineテーマ")
AgGrid(df, theme="alpine")

st.text("balhamテーマ")
AgGrid(df, theme="balham")

st.text("materialテーマ")
AgGrid(df, theme="material")


st.text("カラム幅の自動フィット有効")
AgGrid(df, theme="alpine", fit_columns_on_grid_load=True)

st.text("balhamテーマ、高さ固定")
AgGrid(df, theme="alpine", height=200)

st.text("GridOptionBuilderを使ってカスタマイズ")

waku_cellsytle_jscode = JsCode(
    """
function(params) {
    if(params.value == "1") {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    } else if(params.value == "2") {
        return {
            'color': 'white',
            'backgroundColor': 'black'
        }
    } else if(params.value == "3") {
            return {
                'color': 'white',
                'backgroundColor': 'red'
            }
    } else if(params.value == "4") {
            return {
                'color': 'white',
                'backgroundColor': 'blue'
            }
    } else if(params.value == "5") {
            return {
                'color': 'black',
                'backgroundColor': 'yellow'
            }
    } else if(params.value == "6") {
            return {
                'color': 'white',
                'backgroundColor': 'green'
            }
    } else if(params.value == "7") {
            return {
                'color': 'black',
                'backgroundColor': 'orange'
            }
    } else if(params.value == "8") {
            return {
                'color': 'black',
                'backgroundColor': 'pink'
            }
    } else {
            return {
                'color': 'black',
                'backgroundColor': 'white'
            }
    }
};
"""
)

stable_cellsytle_jscode = JsCode(
    """
function(params) {
    if(params.value.includes("[西]")) {
        return {
            'color': 'red'
        }
    } else if(params.value.includes("[東]")) {
        return {
            'color': 'blue'
        }
    } else if(params.value.includes("[地]")) {
        return {
            'color': 'brown'
        }
    } else {
            return {
                'color': 'black',
                'backgroundColor': 'white'
            }
    }
};
"""
)

sex_cellsytle_jscode = JsCode(
    """
function(params) {
    if(params.value.includes("牝")) {
        return {
            'color': 'red'
        }
    } else if(params.value.includes("牡")) {
        return {
            'color': 'blue'
        }
    } else {
            return {
                'color': 'black',
                'backgroundColor': 'white'
            }
    }
};
"""
)

odds_cellsytle_jscode = JsCode(
    """
function(params) {
    if(params.value < 10.0) {
        return {
            'color': 'red'
        }
    }
};
"""
)

top3_cellsytle_jscode = JsCode(
    """
function(params) {
    if(params.data.着順 == "1") {
        return {
            'backgroundColor': '#ffffe5'
        }
    } else if(params.data.着順 == "2") {
        return {
            'backgroundColor': '#e5ffff'
        }
    } else if(params.data.着順 == "3") {
            return {
                'backgroundColor': '#ffefff'
            }
    } else if(["除","取","中"].includes(params.data.着順)) {
            return {
                'backgroundColor': '#dfdfdf'
            }
    }
};
"""
)

gb = GridOptionsBuilder.from_dataframe(df, min_width="100px")
gb.configure_pagination(False)
gb.configure_default_column(groupable=False, value=True, enableRowGroup=False, editable=False, resizable=False)
gb.configure_column("枠番", cellStyle=waku_cellsytle_jscode)
gb.configure_column("調教師", cellStyle=stable_cellsytle_jscode)
gb.configure_column("性齢", cellStyle=sex_cellsytle_jscode)
gb.configure_column("単勝", cellStyle=odds_cellsytle_jscode)
other_opts = {"surpressColumnVirtualization": True}
gb.configure_grid_options(**other_opts)
gridOptions = gb.build()
gridOptions['getRowStyle'] = top3_cellsytle_jscode

AgGrid(df, theme="alpine", gridOptions=gridOptions, allow_unsafe_jscode=True, fit_columns_on_grid_load=True)
