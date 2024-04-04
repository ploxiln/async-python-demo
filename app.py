import os

import httpx
from fastapi import FastAPI, Response


HTTPBIN = os.environ.get("HTTPBIN", "http://localhost:8080")
# NUMREQS = os.environ.get("NUMREQS", "3")

app = FastAPI(title="Async Python Demo")


@app.get("/health-a")
async def health_a() -> Response:
    return Response(content="OK\n", media_type="text/plain")


@app.get("/health-s")
def health_s() -> Response:
    return Response(content="OK\n", media_type="text/plain")


def sync_http_req(url: str) -> str:
    # inefficient: no connection re-use
    with httpx.Client() as client:
        return client.get(url).text


async def async_http_req(url: str) -> str:
    # inefficient: no connection re-use
    client = httpx.AsyncClient()
    resp = await client.get(url)
    return resp.text


@app.get("/single")
async def single() -> Response:
    # buggy
    resp = sync_http_req(HTTPBIN + "/delay/1")
    return Response(content=resp, media_type="text/plain")
