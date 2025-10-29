from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.core.lexer import Lexer

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.get("/")
async def root():
    return {"message": "Platter Compiler Backend is running"}

@app.post("/analyze")
async def analyze_code(input_data: CodeInput):
    """Analyze Platter code and return lexemes"""
    try:
        lexer = Lexer(input_data.code)
        tokens = []
        
        while True:
            token = lexer.get_next_token()
            if token is None:
                break
            tokens.append({
                "type": token.type,
                "value": token.value,
                "line": token.line,
                "col": token.col
            })
        
        return {"tokens": tokens, "success": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Lexical analysis failed: {str(e)}")