from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


#human readable
@app.get("/home")
def home():
    return( {'message': "This is the message from the VM3 "})