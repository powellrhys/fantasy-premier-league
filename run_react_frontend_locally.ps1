# Enter frontend directory
cd frontend-react

# Build react project
npm run build

# Return to root
cd ..

# Run application using uvicorn
uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 --reload
