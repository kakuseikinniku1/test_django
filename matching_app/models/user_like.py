from django.contrib.auth import get_user_model
from django.db import models

from matching_app.models.base import BaseModel

class UserLike(BaseModel):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    class META:
        unique_together = ("sender", "receiver")
    
    def __str__(self) -> str:
        return f"{self.sender.username} likes {self.receiver.username}"