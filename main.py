from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sympy as sp

app = FastAPI(title="Motor Matemático de Cálculo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MathRequest(BaseModel):
    expression: str

@app.post("/solve")
async def solve_math(data: MathRequest):
    try:
        x = sp.Symbol('x')
        expr = sp.sympify(data.expression)
        result = sp.integrate(expr, x)
        latex_res = sp.latex(result)

        return {
            "status": "success",
            "solution": f"{latex_res} + C"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Expresión no válida: {str(e)}")
