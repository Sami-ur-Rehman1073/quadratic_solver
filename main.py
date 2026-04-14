from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import math
import socket

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/solve")
def solve(a: float, b: float, c: float):

    discriminant = b**2 - 4*a*c
    server_ip = socket.gethostbyname(socket.gethostname())

    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = {"type": "Real & Different Roots", "root1": r1, "root2": r2}

    elif discriminant == 0:
        r = -b / (2*a)
        result = {"type": "Real & Equal Roots", "root1": r, "root2": r}

    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        result = {
            "type": "Complex Roots",
            "root1": f"{real} + {imag}i",
            "root2": f"{real} - {imag}i"
        }

    return JSONResponse({
        "result": result,
        "server_ip": server_ip
    })