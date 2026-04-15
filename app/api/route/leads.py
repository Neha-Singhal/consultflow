from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.database import  engine, Base, get_db
from app.models.user import User
from app.models.lead import Lead
from app.schemas.user import UserCreate, UserResponse
from app.schemas.lead import  LeadCreate , LeadResponse, EmailRequest, EmailResponse
from app.core.security import oauth2_scheme, hash_password, verify_password, create_access_token,verify_token, decode_access_token

router = APIRouter(prefix="/leads", tags=["leads"])

@router.post("", response_model=LeadResponse)
def create_lead(
    lead: LeadCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_access_token(token)
    email = payload.get("sub")

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    new_lead = Lead(
        name=lead.name,
        email=lead.email,
        company=lead.company,
        owner_id=user.id
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    return new_lead


"""GET ALL LEADS"""
@router.get("/",response_model=list[LeadResponse])
def get_leads(
        token:str = Depends(oauth2_scheme),
        db: Session = Depends(get_db),
):
    payload = decode_access_token(token)
    email = payload.get("sub")

    user = db.query(User).filter(User.email == email).first()

    leads = db.query(Lead).filter(Lead.owner_id == user.id).all()

    return leads



# GET SINGLE LEAD
@router.get("/{lead_id}", response_model=LeadResponse)
def get_lead(
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

    return lead

# DELETE LEAD
@router.delete("/{lead_id}")
def delete_lead(
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

    db.delete(lead)
    db.commit()

    return {"message": "Lead deleted"}
