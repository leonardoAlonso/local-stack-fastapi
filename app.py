from fastapi import FastAPI, UploadFile, File
import boto3
import os
import dotenv

dotenv.load_dotenv()


app = FastAPI()

# AWS Credentials

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

ENDPOINT_URL = f"http://localhost:4566"


@app.post("/uploadfile/")
async def upload_image(file: UploadFile = File(...)):
    s3 = boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION,
    )
    s3.upload_fileobj(file.file, AWS_BUCKET_NAME, file.filename)
    image_url = f"{ENDPOINT_URL}/{AWS_BUCKET_NAME}/{file.filename}"
    return {"image_url": image_url}
