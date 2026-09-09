from fastapi import FastAPI
import uvicorn
from controllers import user_controller
from fastapi.middleware.cors import CORSMiddleware

# créer une instance de FastAPI
app = FastAPI()

app.include_router(user_controller.router)
app.add_middleware(CORSMiddleware, allow_headers=['*'],allow_methods=['*'],allow_origins=['*'])

if __name__ == '__main__':
    # exposer FastAPI sur le port 8000
    uvicorn.run(
        'main:app', 
        host='127.0.0.1',
        port=8000,
        reload=True
    )