import requests
import os

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
API_KEY = os.environ["API_KEY"]
headers = {"Authorization": f"Bearer {API_KEY}"}

async def homepage(request):
	payload = {"inputs": "When did Brady win his first chip?"}
	response = requests.post(API_URL, headers=headers, json=payload)
	return JSONResponse(response.json()[0])


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
