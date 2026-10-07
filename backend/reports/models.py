# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class IssueReport(models.Model):

    class Category(models.TextChoices):
        ELECTRICAL = "electrical", "Electrical"
        PLUMBING = "plumbing", "Plumbing"
        CLEANLINESS = "cleanliness", "Cleanliness"
        INFRASTRUCTURE = "infrastructure", "Infrastructure"
        INTERNET = "internet", "Internet"
        OTHER = "other", "Other"

    class Priority(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"
        CRITICAL = "critical", "Critical"

    class Status(models.TextChoices):
        REPORTED = "reported", "Reported"
        ACKNOWLEDGED = "acknowledged", "Acknowledged"
        IN_PROGRESS = "in Progress", "In Progress"
        RESOLVED = "resolved", "Resolved"
        REJECTED = "rejected", "Rejected"

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=Category.choices,
    )

    location = models.CharField(max_length=200)

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.REPORTED,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="issue_reports",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
