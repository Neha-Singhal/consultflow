from pydantic import BaseModel, EmailStr

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    company: str | None = None


class LeadResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    company: str | None

    class Config:
        from_attributes = True


class EmailRequest(BaseModel):
    lead_name: str
    company: str


class EmailResponse(BaseModel):
    email: str
