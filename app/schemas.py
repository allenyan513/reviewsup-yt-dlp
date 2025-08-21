from pydantic import BaseModel

class VideoRequest(BaseModel):
    url: str

class VideoInfo(BaseModel):
    title: str
    uploader: str
    duration: float
    # thumbnail: str
    video_url: str