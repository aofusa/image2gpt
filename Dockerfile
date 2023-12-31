FROM python:3-slim

WORKDIR /app

COPY . /app
COPY requirements.txt /app

ENV TESSERACT_PATH /usr/bin/tesseract

RUN apt update && apt install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-jpn tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "image2text.py"]