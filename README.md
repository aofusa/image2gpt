# OCRとChatGPT 統合アプリ

このアプリケーションは、画像からテキストを抽出し、それを ChatGPT に送信することができる簡単な Web アプリです。  
公開されているアプリはこちら。  
https://aofusa.github.io/ocr-chatgpt-app/


## インストール

必要なパッケージをインストールするには以下のコマンドを実行してください。

```bash
pip install -r requirements.txt
```

以下のコマンドでアプリケーションを実行できます。

```bash
streamlit run image2text.py
```


## Docker での実行

Docker を使用してアプリケーションを実行するには、以下のコマンドを実行します。

```bash
docker build -t ocr-chatgpt-app .
docker run -p 8501:8501 ocr-chatgpt-app
```

アプリケーションは http://localhost:8501 でアクセス可能です。


## 使い方

1. ChatGPT の API_KEY を取得し画面上より設定します
2. 画像ファイルをアップロードして、Tesseract OCR でテキストを抽出します。
3. テキストを編集し、「ChatGPTに送信」ボタンをクリックして ChatGPT に送信します。
4. ChatGPT からのレスポンスが表示されます。


## ライセンス

このプロジェクトは [Apache ライセンス 2.0](https://licenses.opensource.jp/Apache-2.0/Apache-2.0.html) のもとで提供されています。

