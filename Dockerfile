FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

ARG manager_id
ENV env_manager_id $manager_id

ARG leagues
ENV eng_leagues $leagues

ENV password 123

RUN python update_data.py

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["Home.py"]
