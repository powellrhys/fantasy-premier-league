# Stage 1: Build React frontend
FROM node:18-alpine as build-frontend

# Set the working directory for frontend
WORKDIR /frontend

# Copy package.json and install frontend dependencies
COPY ./frontend-react/package.json ./frontend-react/package-lock.json ./
RUN npm install

# Copy the entire frontend code and build the React app
COPY ./frontend-react/ ./
RUN npm run build

# Stage 2: Build Python backend
FROM python:3.10-slim

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

# Set the working directory for backend
WORKDIR /app

# Copy backend requirements and install Python dependencies
COPY ./backend/api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY ./backend/ .

# Copy the built React frontend from the previous stage
COPY --from=build-frontend /frontend/dist /app/frontend/dist

# Expose the necessary port
EXPOSE 8000

# WORKDIR /app/api

# Run FastAPI with Uvicorn, serving both the API and the React frontend
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
