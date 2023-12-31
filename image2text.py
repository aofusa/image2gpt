import streamlit as st
import pytesseract
from PIL import Image
from chatgpt_request import ChatGPTRequest

def main():
    st.title("ChatGPTとOCRを組み合わせたアプリ")

    # ChatGPTのAPIキーとエンドポイントをユーザーに入力させる
    api_key = st.text_input("ChatGPT APIキーを入力してください:")

    if not api_key:
        st.warning("APIキーが入力されていません。")
        st.stop()

    # ChatGPTRequestのインスタンスを作成
    chatgpt_request = ChatGPTRequest(api_key)

    # ファイルアップロードのウィジェット
    uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # アップロードされた画像を表示
        st.image(uploaded_file, caption="アップロードされた画像", use_column_width=True)

        # Tesseract OCRでテキストを抽出
        text = extract_text(uploaded_file)
        st.subheader("Tesseract OCRからのレスポンス:")

        # ユーザーがテキストを編集
        edited_text = st.text_area("テキストを編集", text)
        print(text)
        print(edited_text)

        # ChatGPTにテキストを送信するボタン
        if st.button("ChatGPTに送信"):
            with st.spinner("ChatGPTからのレスポンスを待っています..."):
                if edited_text:
                    # ChatGPTにリクエストを送信
                    response = chatgpt_request.send_request(edited_text)

                    # ChatGPTからのレスポンスを表示
                    st.subheader("ChatGPTからのレスポンス:")
                    print(response)
                    st.text(response)

def extract_text(uploaded_file):
    # アップロードされた画像をPIL Imageに変換
    image = Image.open(uploaded_file)

    # Tesseract OCRを使用してテキストを抽出
    text = pytesseract.image_to_string(image, lang="jpn+jpn_vert")

    return text

if __name__ == "__main__":
    main()
