# Use a lightweight Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_CONFIG_DIR=/app/.streamlit \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PORT=8501

# Set working directory
WORKDIR /app

# Install system dependencies and Microsoft ODBC Driver 17 for SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    git \
    gnupg \
    unixodbc \
    unixodbc-dev \
    libgssapi-krb5-2 \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip poetry

# --- COPY ALL PROJECT FILES before installing dependencies ---
COPY . /app
COPY frontend/entrypoint.sh /app/entrypoint.sh

# Enable execution of the entrypoint script
RUN chmod +x /app/entrypoint.sh

# Install dependencies (frontend + main)
RUN poetry install --only main --extras "frontend"

# Expose Streamlit port
EXPOSE 8501

# Entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
