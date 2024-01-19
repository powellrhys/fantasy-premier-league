FROM python:3.9-slim

COPY frontend/ /app
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN apt-get update \
 && apt-get install --yes --no-install-recommends \
        apt-transport-https \
        curl \
        gnupg \
        unixodbc-dev \
 && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
 && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install --yes --no-install-recommends msodbcsql17 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/*

# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# RUN apt-get update
# RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
# RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools


# RUN apt-get update \
#     && apt-get install unixodbc -y \
#     && apt-get install freetds-dev -y \
#     && apt-get install freetds-bin -y \
#     && apt-get install tdsodbc -y \
#     && apt-get install --reinstall build-essential -y

# RUN ACCEPT_EULA=Y apt-get install msodbcsql17 --assume-yes

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["Home.py"]
