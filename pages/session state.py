import streamlit as st

st.markdown("## session stateを使ったカウンターのサンプル")

if 'count' not in st.session_state:
    st.session_state["count"] = 0

if st.button("カウントアップ", key=0):
    st.session_state["count"] += 1

if st.button("カウントダウン", key=1):
    st.session_state["count"] -= 1

st.write("カウント", st.session_state["count"])

st.code("""
    import streamlit as st

    st.markdown("## session stateを使ったカウンターのサンプル")

    if 'count' not in st.session_state:
        st.session_state["count"] = 0

    if st.button("カウントアップ", key=0):
        st.session_state["count"] += 1

    if st.button("カウントダウン", key=1):
        st.session_state["count"] -= 1

    st.write("カウント", st.session_state["count"])
""")
