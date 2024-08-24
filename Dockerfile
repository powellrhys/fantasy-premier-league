# Stage 1: Build the React application
FROM node:18 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json for frontend
COPY frontend-react/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the entire frontend code and build the React app
COPY frontend-react/ ./
RUN npm run build

# Stage 2: Build Python backend and include the React build
FROM python:3.11-slim

# Set working directory for backend
WORKDIR /app

# Copy requirements file and install dependencies
COPY backend/api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies
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

# Copy FastAPI application code
COPY backend /app/backend

# Copy the built React frontend from the previous stage
COPY --from=build /app/dist /app/frontend-react/dist

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
