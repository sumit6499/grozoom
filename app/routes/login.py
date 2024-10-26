from fastapi import FastAPI

app = FastAPI()

@app.post('/login')
def login()->dict:
    return {"success":True,"msg":"login success"}

