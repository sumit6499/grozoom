from fastapi import FastAPI

app=FastAPI()

@app.get('/login')
async def user_login():
    return {"user":"login success"}
