from http import cookies
from django.shortcuts import render , redirect
from .models import Certifications, Skills , Projects , Experience , Project_skills , Experience_skills
from .model_class_for_projects import Projects_support
from .model_class_for_experience import Experience_support
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
def skills(request) :
    # if request.user.is_authenticated :
        skills_data = Skills.objects.all()
        return render(request , 'skills.html' , {"skills_data" : skills_data})
    # else :
    #     messages.info(request , 'Illegal Access')
    #     return redirect('..')

def certifications(request) :
    data = Certifications.objects.all()
    return render(request , 'certifications.html' , {"skills_data" : data})

def projects(request) :
    projects_data = Projects.objects.all()
    data_ = []
    for data in projects_data :
        skills_ = Project_skills.objects.filter(project_id = data).only("skill_id")
        skill = []
        for i in skills_ :
            skill.append(i.skill_id.image_link)
        p = Projects_support(data , skill)
        data_.append(p)
    print(data_)
    return render(request , 'projects.html' , {"data" : data_})

def projectswithskill(request , slug) :
    projects_data = Projects.objects.all()
    data_ = []
    is_proj = False
    is_exp = False
    for data in projects_data :
        skills_ = Project_skills.objects.filter(project_id = data).only("skill_id")
        skill = []
        is_skill = False
        for i in skills_ :
            if(i.skill_id.skill_name == slug) :
                is_skill = True
            skill.append(i.skill_id.image_link)
        if(is_skill) :
            is_proj = True
            p = Projects_support(data , skill)
            data_.append(p)
    experience_data = Experience.objects.all()
    for data in experience_data :
        skills_ = Experience_skills.objects.filter(experience_id = data).only("skill_id")
        skill = []
        is_skill = False
        for i in skills_ :
            if(i.skill_id.skill_name == slug) :
                is_skill = True
            skill.append(i.skill_id.image_link)
        if(is_skill and is_proj == False) :
            p = Experience_support(data , skill)
            data_.append(p)
    print(data_)
    if(is_proj) :
        return render(request , 'projects.html' , {"data" : data_})
    else :
        return render(request , 'experience.html' , {"data" : data_})



def experience(request) :
    experience_data = Experience.objects.all()
    data_ = []
    for data in experience_data :
        skills_ = Experience_skills.objects.filter(experience_id = data).only("skill_id")
        skill = []
        for i in skills_ :
            skill.append(i.skill_id.image_link)
        p = Experience_support(data , skill)
        data_.append(p)
    return render(request , 'experience.html' , {"data" : data_})
# Create your views here.
