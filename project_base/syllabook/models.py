from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=100)
    contact_hours = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    textbook = RichTextField(blank=True, null=True)
    other_supplementary_material = RichTextField(blank=True, null=True)
    course_description = RichTextField(blank=True, null=True)
    prerequisites = models.CharField(max_length=100)
    corequisites = models.CharField(max_length=100)
    course_classification = models.CharField(max_length=100)
    course_objective = RichTextField(blank=True, null=True)
    course_outcomes = RichTextField(blank=True, null=True)
    student_outcome_addressed_by_the_course = RichTextField(blank=True, null=True)
    course_topics = RichTextField(blank=True, null=True)
    prepared = models.CharField(max_length=100)
    noted = models.CharField(max_length=100)
    marked = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.course_code

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
