from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from model.request import Request
from services.call_llm import call

load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def test():
    return { 'text': 'API up and running!' }


@app.post('/response')
def response(request:Request):
    answer = call(request.query, request.context_documents)
    return StreamingResponse(answer, media_type="text/plain")