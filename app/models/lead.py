from sqlalchemy import Column , Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base



class Lead(Base):
    __tablename__ ="Leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String,nullable=False)
    company = Column(String)

    owner_id = Column(Integer,ForeignKey("users.id"))

    owner = relationship("User")
