import os
from fastapi import FastAPI, UploadFile, File, staticfiles, Request, WebSocket, responses
from pydantic import BaseModel

app = FastAPI(
    title="API",
    description="API for managing a blog",
    version="0.1.0"
    )

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

IMAGES = 'Images'
# app.mount(IMAGES, staticfiles(directory=IMAGES), name="static")

if not os.path.exists(IMAGES):
    os.makedirs(IMAGES)

blogs = [
    {
    "id": 1,
    "title": "ATH v BARC",
    "content": "2 - 4"
    },
    {
    "id": 2,
    "title": "The World",
    "content": "12 - 15"
    },
    {
    "id": 3,
    "title": "Chelsea v Real Madrid",
    "content": "1 - 1"
    }
]
class Blog(BaseModel):
    title: str
    content: str

@app.get("/")
async def main():
    return "My API is working"


@app.get("/posts")
async def get_blogs():
    return blogs

@app.get("/posts/{id}")
async def get_blog(id: int):
    return blogs[id - 1]


@app.delete("/posts/{id}")
def delete_blog(id: int):
    return f" blog with id: {id} was successfully deleted"
    
    
@app.post("/upload-image")
async def upload_img(request: Request, data: UploadFile = File(...)):
    filepath = os.path.join(IMAGES, data.filename)
    with open(filepath, 'wb') as buffer:
        buffer.write(await data.read())
    url = f"{request.base_url}static/{data.filename}"
    return f"{data.filename} has been uploaded to {url}"

@app.post("/posts")
async def create_blog(data: Blog):
    return {"message": "Blog created successfully", "data": {"title": data.title, "content": data.content}}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
        
@app.get("/page")
async def get():
    return responses.HTMLResponse(html)