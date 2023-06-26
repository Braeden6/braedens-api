from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv()


from app.api.v1.myresume import router as myresume_router

app = FastAPI()

app.include_router(myresume_router, prefix="/api/v1")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://braedensconsulting.com", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)




# For health checks
@app.get("/")
async def root():
    return "ok"



