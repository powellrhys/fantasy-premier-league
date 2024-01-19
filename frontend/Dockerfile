FROM python:3.9-slim

COPY frontend/ /app
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["Home.py"]
