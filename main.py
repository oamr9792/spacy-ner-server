import os
from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

class Text(BaseModel):
    text: str

@app.post("/ner")
async def extract_entities(text: Text):
    doc = nlp(text.text)
    entities = [
        {
            "entity": ent.text,
            "type": ent.label_,
            "score": 1.0
        }
        for ent in doc.ents
    ]
    return {"entities": entities}

@app.get("/")
async def root():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
