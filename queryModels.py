from pydantic import BaseModel

class Links(BaseModel):
	links: list


class Session(BaseModel):
	session_id: int