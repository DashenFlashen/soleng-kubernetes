from fastapi import FastAPI
import time

app = FastAPI()
sleep_duration = 3

@app.get("/")
async def json_response():
    print(f'Sleeping for {sleep_duration} seconds...')
    time.sleep(sleep_duration)
    return {"message": "Hello, world!"}
