from fastapi import *
import easyocr

reader = easyocr.Reader(['th','en'],gpu=False)
app = FastAPI()

def obj_str(obj):
    text = '{"data":['
    for i, data in enumerate(obj):
        text += '{"text":"'
        text += data[1] + '"'
        text += ',"probability":'
        text += str(data[2])
        text += "}"
        if len(obj) - i != 1:
            text += ","
    text += ']}'
    return text

@app.post("/ocr")
async def up_img(file: UploadFile = File(...)):
    size = await file.read()
    data=obj_str(reader.readtext(size))
    return data
