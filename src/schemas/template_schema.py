from pydantic import BaseModel


class TemplateSchema(BaseModel):
    anything: str
