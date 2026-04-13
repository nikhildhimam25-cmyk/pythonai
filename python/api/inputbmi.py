from pydantic import BaseModel
class  bmiinput(BaseModel):
    age:float
    height:float
    weight:float