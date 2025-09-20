from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

@app.get("/")
async def root():
	return FileResponse("holaEspanol.html")

@app.get("/ingles")
async def ingles():
	return FileResponse("holaIngles.html")

@app.get("/frances")
async def frances():
	return FileResponse("holaFrances.html")

@app.get("/italiano")
async def italiano():
	return FileResponse("holaItaliano.html")


#cookies
@app.get("/getFuente")
async def getFuente(request: Request):
	fue = request.cookies.get("fontFamily")
	return JSONResponse({"fontFamily": fue})

@app.post("/setFuente/{fuente}")
async def setFuente(fuente: str, response: Response):
	response = JSONResponse({"mensaje": "fuente guardada"})
	response.set_cookie(key="fontFamily", value=fuente, max_age=60*60);
	return response
