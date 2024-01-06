FROM python:3.10.12

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

CMD ["streamlit", "run", "app.py"]
