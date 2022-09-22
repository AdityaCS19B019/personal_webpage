from django.db import models


class Skills(models.Model) :
    skill_name = models.CharField(max_length=20)
    my_rating = models.CharField(max_length=10)
    Projects_done = models.CharField(max_length=5)
    skill_desc = models.CharField(max_length=200)
    image_link = models.CharField(max_length=300)
    category = models.CharField(max_length=25)

class Projects(models.Model) :
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=20)
    project_duration = models.CharField(max_length=20)
    git_web_link = models.CharField(max_length=200)
    project_type = models.CharField(max_length=40)
    project_abstract = models.TextField()

class Experience(models.Model) :
    experience_no = models.IntegerField()
    company_name = models.CharField(max_length=50)
    Desg = models.CharField(max_length=30)
    duration = models.CharField(max_length=20)
    Desc = models.TextField()

class Project_skills(models.Model) :
    project_id = models.ForeignKey(Projects , on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills , on_delete=models.CASCADE)


class Experience_skills(models.Model) :
    experience_id = models.ForeignKey(Experience , on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills , on_delete=models.CASCADE)

class Certifications(models.Model) :
    Skill_name = models.ForeignKey(Skills , on_delete=models.CASCADE)
    certification_link = models.TextField()
    certified_by = models.CharField(max_length=100)

