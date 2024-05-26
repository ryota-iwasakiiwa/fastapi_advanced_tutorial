from typing import Any

import orjson
from fastapi import FastAPI
from fastapi.responses import Response, ORJSONResponse, HTMLResponse, RedirectResponse, StreamingResponse, FileResponse

some_file_path = "rolikami720p.mp4"

app =FastAPI()

@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(status_code=200, content=html_content)

@app.get("/users/", response_class=HTMLResponse)
async def read_users():
    return generate_html_response()

@app.get("/redirect/", response_class=RedirectResponse)
async def redirect():
    return "https://fastapi.tiangolo.com"

async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes\n"

@app.get("/video/", response_class=StreamingResponse)
async def video():
    return StreamingResponse(fake_video_streamer())

@app.get("/file/", response_class=FileResponse)
async def file():
    return some_file_path


class CustomORJSONResponse(Response):
    media_type = "application/json"
    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)

@app.get("/custom/", response_class=CustomORJSONResponse)
async def custom():
    return {"message": "Hello World"}