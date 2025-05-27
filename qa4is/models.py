from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Role(models.Model):
    name = models.CharField(max_length=100)
    responsibilities = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Industry(models.Model):
    INDUSTRY_CHOICES = [
        ('government', 'Government'),
        ('banking', 'Banking'),
        ('insurance', 'Insurance'),
        ('health_care', 'Health Care'),
        ('hydro_electric', 'Hydro-Electric'),
    ]

    name = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return dict(self.INDUSTRY_CHOICES)[self.name]

class Project(models.Model):
    name = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)
    description = models.TextField()

    def __str__(self):
        return self.name

class Timeline(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    milestones = models.TextField()

    def __str__(self):
        return f"{self.project.name} ({self.start_date} - {self.end_date if self.end_date else 'Ongoing'})"