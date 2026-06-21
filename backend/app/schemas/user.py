from pydantic import BaseModel


class CreateUser(BaseModel):
    user_id: str
    name: str
    description: str
    github_id: str
    qiita_id: str
    x_id: str