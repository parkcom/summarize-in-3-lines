import streamlit as st
import openai
import sys


# UTF-8 인코딩 설정
sys.stdout.reconfigure(encoding="utf-8")


def askGpt(prompt, apikey):
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    gptResponse = response.choices[0].message.content
    return gptResponse


def main():
    st.set_page_config(page_title="요약 프로그램")

    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    with st.sidebar:
        openai_apikey = st.text_input(
            "OpenAI API Key", placeholder="Enter your OpenAI API key", type="password"
        )

        if openai_apikey:
            st.session_state["OPENAI_API"] = openai_apikey
        st.markdown("---")

    st.header("📝 요약 프로그램")
    st.markdown("---")

    text = st.text_area("요약 할 글을 입력하세요", height=300)
    if st.button("요약"):
        prompt = f"""
***Instructions:*** :
- You are an exppert assistant that summarizes text into **Korean language**.
- You task is to summarize the **text** sentences in **Korean language**.
- Your summaries should include the following :
    - Omit duplicate content, but increase the summary weight of duplicate content.
    - Summarize by emphasizing concepts and arguments rather than case evidence.
    - Summarize in 3 lines.
    - Use the format of bullet point.
- text: {text}
"""
        st.info(askGpt(prompt, st.session_state["OPENAI_API"]))


if __name__ == "__main__":
    main()
