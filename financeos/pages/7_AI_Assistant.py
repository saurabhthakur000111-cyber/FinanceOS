import streamlit as st
import os
from openai import OpenAI


st.set_page_config(
    page_title="FinanceOS AI Assistant",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 FinanceOS AI Assistant")

st.write(
    "AI-powered financial analysis assistant"
)


api_key = os.getenv("OPENAI_API_KEY")


if api_key:

    client = OpenAI(
        api_key=api_key
    )


    question = st.text_area(
        "Ask FinanceOS AI",
        placeholder="Example: Explain Reliance stock fundamentals"
    )


    if st.button("Generate Analysis"):

        if question:

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content":
                        "You are a professional finance analyst."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )


            st.subheader(
                "AI Response"
            )


            st.write(
                response.choices[0].message.content
            )


else:

    st.warning(
        "OPENAI_API_KEY not configured"
    )


    st.info(
        """
        Add your API key:

        export OPENAI_API_KEY="your_key_here"

        Then restart Streamlit.
        """
    )


st.divider()


st.subheader(
    "FinanceOS AI Capabilities"
)


features = [
    "Stock explanation",
    "Financial statement analysis",
    "Risk summary",
    "Portfolio insights",
    "Investment report generation"
]


for item in features:
    st.write(
        "✅",
        item
    )
