from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from .auth import get_current_user

router = APIRouter()

class EmailRequest(BaseModel):
    recipients: List[str]
    subject: str
    body: str

class EmailLog(BaseModel):
    id: int
    recipient: str
    subject: str
    sent_at: str
    status: str

# Mock email logs
MOCK_EMAIL_LOGS = []

@router.post("/send")
async def send_email(email: EmailRequest, current_user: str = Depends(get_current_user)):
    # In production, integrate with Brevo API
    for recipient in email.recipients:
        log = {
            "id": len(MOCK_EMAIL_LOGS) + 1,
            "recipient": recipient,
            "subject": email.subject,
            "sent_at": "2023-01-01T00:00:00Z",
            "status": "sent"
        }
        MOCK_EMAIL_LOGS.append(log)
    return {"message": f"Email sent to {len(email.recipients)} recipients"}

@router.get("/logs", response_model=List[EmailLog])
async def get_email_logs(current_user: str = Depends(get_current_user)):
    return MOCK_EMAIL_LOGS