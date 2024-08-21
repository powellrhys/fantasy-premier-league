cd frontend-react

npm run build

cd ..

uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 --reload