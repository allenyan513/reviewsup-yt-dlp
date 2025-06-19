from fastapi import FastAPI, HTTPException
from app.schemas import VideoRequest, VideoInfo
from app.parser import extract_video_info
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Video Info Parser API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/parse", response_model=VideoInfo)
async def parse_video(req: VideoRequest):
    try:
        info = extract_video_info(req.url)
        return info
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
