from pyexpat.errors import messages

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(lead_name: str, company: str) -> str:
    return f"""
Hi {lead_name},

I came across {company} and was really impressed by your work.

I’d love to connect and explore how we can collaborate.

Best regards,
Your Name
"""