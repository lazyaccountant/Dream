import os
import requests
import sys
import time
from PIL import Image
import io
import subprocess
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("TOKEN")


API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {token}"}


def loading_animation():
    chars = "/—\|"
    for _ in range(100):
        sys.stdout.write("\rDreaming... " + chars[_ % len(chars)])
        sys.stdout.flush()
        time.sleep(0.1)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def dream():
	prompt = input("Dream: ")
	loading_animation()

	image_bytes = query({
		"inputs": prompt,
		"wait_for_model": "True"
		})

	img_bytes = io.BytesIO(image_bytes)
	image = Image.open(img_bytes)
	image.save("test.jpeg")

	subprocess.run("termux-open test1.jpg", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)

if __name__ == "__main__":
	dream()
