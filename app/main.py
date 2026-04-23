from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.route import auth, leads, ai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(leads.router)
app.include_router(ai.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
    "https://your-app.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "ConsultFlow AI running"}