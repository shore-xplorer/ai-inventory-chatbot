import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import openai

load_dotenv()

st.set_page_config(page_title="AI Inventory Chatbot", layout="wide")
st.title("🧊 AI Inventory Chatbot – Frozen Foods Ops")

st.sidebar.header("Upload Inventory CSV")
uploaded_file = st.sidebar.file_uploader("Upload inventory.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📦 Current Inventory")
    st.dataframe(df)
st.divider()
st.subheader("🤖 Ask your inventory  question")

question = st.text_input("What do you want to know about this inventory?")

if question and uploaded_file:
    inventory_preview = df.head(50).to_csv(index=False)

    prompt = f"""
You are an inventory operations analyst for a frozen foods department.

Here is the current inventory CSV preview:
{inventory_preview}

Answer this question clearly and concisely:
{question}
"""

   with st.spinner("Analyzing inventory..."):
       response = openai.responses.create(
           mode1="gpt-4.1-mini",
           input=prompt
        )

        answer = response.output_text
        st.success(answer)

{df.head(50).to_csv(index=False)}

Question: {user_question}
"""

    with st.spinner("Thinking..."):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        answer = response.output_text
        st.success(answer)
    user_query = st.text_input("Ask your inventory question:")

    if user_query:
        inventory_summary = df.head(20).to_string()

        prompt = f"""
        You are an AI inventory optimization analyst for a grocery frozen foods department.
        Inventory snapshot:
        {inventory_summary}

        Question: {user_query}
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        st.markdown("### 🤖 AI Response")
        st.write(response.choices[0].message.content)
else:
    st.info("Upload a CSV inventory file to begin.")
