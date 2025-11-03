import streamlit as st
from sentiment_engine import predict_sentiment
from database_handler import *
import pandas as pd

# Header section
st.set_page_config(page_title="Sentiment Assistant", page_icon="💬", layout="centered")

st.title("💬 Sentiment Assistant")
st.write("Trợ lý phân tích cảm xúc văn bản tiếng việt")

# Input section
text_input = st.text_area("Nhập đoạn văn bản cần phân tích:")

if st.button("Phân tích cảm xúc"):
    try:
        analysis_result = predict_sentiment(text_input)
        save_sentiment_to_db(analysis_result)
        st.success(f"✅ Cảm xúc: **{analysis_result['sentiment']}**")
    except ValueError as e:
        st.warning(f"⚠️ {e}")

# History section
st.divider()

sentiments_history = get_all_sentiments()
if sentiments_history:
    df = pd.DataFrame(sentiments_history, columns=["Văn bản", "Cảm xúc", "Thời gian"])

    PAGE_SIZE = 50

    # Init session_state for storing number of displayed rows
    if "rows_displayed" not in st.session_state:
        st.session_state.rows_displayed = PAGE_SIZE

    st.subheader("📊 Lịch sử phân tích cảm xúc")

    # Cut DataFrame by number of displayed rows
    df_display = df.head(st.session_state.rows_displayed)

    # Show the table
    st.table(df_display)

    # If DataFrame still contains data, shows the load more button
    if len(df) > st.session_state.rows_displayed:
        if st.button("⬇️ Tải thêm"):
            st.session_state.rows_displayed += PAGE_SIZE
            st.rerun()
else:
    st.info("ℹ️ Lịch sử phân tích rỗng!")
