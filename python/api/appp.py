import uvicorn
from fastapi import FastAPI


app=FastAPI()
@app.get("/")
def name():
    return{"hello":"this is api key  "}

# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=8000)
# @app.get('/')
# def index():
#     return {"message":"Hello Coder Roots"}

# @app.get('/name')
# def printName():
#     return {"message":"Hello Baljinder"}

# @app.get('/{naam}')
# def printNaam(naam:str):
#     return {'Name is':f"{naam}"}


if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1', port=8000) 



