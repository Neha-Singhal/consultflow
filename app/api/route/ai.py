from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.database import  engine, Base, get_db
from app.models.user import User
from app.models.lead import Lead
from app.schemas.user import UserCreate, UserResponse
from app.schemas.lead import  LeadCreate , LeadResponse, EmailRequest, EmailResponse
from app.core.security import oauth2_scheme, hash_password, verify_password, create_access_token,verify_token, decode_access_token
from app.services.ai_service import generate_email
from app.services.email_service import send_email

router = APIRouter(prefix="/ai")

@router.post("/generate_email", response_model=EmailResponse)
def ai_generate_email(
    request: EmailRequest,
    token: str = Depends(oauth2_scheme)
):

    email_text = generate_email(
        lead_name=request.lead_name,
        company=request.company
    )

    return {"email": email_text}


@router.post("/send-email")
def send_ai_email(
    lead_id: int,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_access_token(token)
    email = payload.get("sub")

    user = db.query(User).filter(User.email == email).first()

    lead = db.query(Lead).filter(
        Lead.id == lead_id,
        Lead.owner_id == user.id
    ).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    email_text = generate_email(lead.name, lead.company)

    send_email(
        to_email=lead.email,
        subject=f"Hello {lead.name}",
        body=email_text
    )

    return {
        "message": "Email sent",
        "preview": email_text
    }