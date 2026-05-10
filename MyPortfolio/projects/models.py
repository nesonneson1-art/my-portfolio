from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50) # e.g., Java, Python
    image = models.ImageField(upload_to='project_images/')
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     message = models.TextField()

     def __str__(self):
        return self.name

class Profile(models.Model):
     name = models.CharField(max_length=100)
     profile_pic = models.ImageField(upload_to='profile_pics/')
     linkedin = models.URLField()
     github = models.URLField()

     def __str__(self):
        return self.name
     
class Profile(models.Model):
    # ஏற்கனவே உள்ளவை...
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    linkedin = models.URLField()
    github = models.URLField()
    
    # புதுசா சேர்க்க வேண்டியவை:
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True, help_text="உங்களைப் பற்றி இங்கே எழுதவும்")
    portfolio_title = models.CharField(max_length=200, default="My Project Portfolio")
    sub_title = models.CharField(max_length=200, default="Java Developer | Django Enthusiast")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True) # இந்த வரியைச் சேர்க்கவும்
    def __str__(self):
        return self.name