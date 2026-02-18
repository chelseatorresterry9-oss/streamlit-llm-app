from dotenv import load_dotenv

load_dotenv()
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

# アプリのタイトルと説明
st.title("健康アドバイザーAI 💪🥗😴")
st.write("筋トレ、栄養学、睡眠の専門家があなたの質問に答えます！")
st.write("専門家を選択して、質問を入力してください。")

# 専門家を選択するラジオボタン
expert_type = st.radio(
    "専門家を選択してください：",
    ("筋トレの専門家", "栄養学の専門家", "睡眠の専門家")
)

# 入力フォーム
user_input = st.text_input("質問を入力してください：")

# LLMに質問を送信して回答を得る関数
def get_ai_response(expert, question):
    # 専門家に応じたシステムメッセージを設定
    if expert == "筋トレの専門家":
        system_message = "あなたは筋トレとフィットネスの専門家です。科学的根拠に基づいたトレーニング方法やフォーム、プログラムについてアドバイスしてください。"
    elif expert == "栄養学の専門家":
        system_message = "あなたは栄養学の専門家です。健康的な食事、栄養バランス、サプリメントについて科学的な知識を基にアドバイスしてください。"
    else:  # 睡眠の専門家
        system_message = "あなたは睡眠の専門家です。質の高い睡眠を得るための方法、睡眠リズム、睡眠環境について専門的にアドバイスしてください。"
    
    # ChatOpenAIのインスタンスを作成
    chat = ChatOpenAI(model="gpt-4o-mini")
    
    # メッセージを作成してLLMに送信
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=question)
    ]
    
    response = chat.invoke(messages)
    return response.content

# ボタンが押されたら実行
if st.button("質問する"):
    if user_input:
        with st.spinner("回答を生成中..."):
            answer = get_ai_response(expert_type, user_input)
            st.success("回答：")
            st.write(answer)
    else:
        st.warning("質問を入力してください。")