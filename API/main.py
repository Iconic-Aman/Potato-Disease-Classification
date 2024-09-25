from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


app = FastAPI()

MODEL = tf.keras.models.load_model("model.keras")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)  #expand the dimension  1D->2D , 2D-> 3D  
    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    accuracy = np.max(predictions[0])
    return {
        'class': predicted_class,
        'accuracy': float(accuracy)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)