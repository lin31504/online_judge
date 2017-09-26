from django.db import models
import datetime
from django.contrib.auth.hashers import make_password, check_password
from multiselectfield import MultiSelectField
# Create your models here.

class member(models.Model):
    name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    AC = models.IntegerField(default=0)
    overview = models.CharField(max_length=500, default="No any introduce!")
    pphone = models.CharField(blank=True,default=' ',max_length=10)
    LANGUAGE_CHOICES = (
        ('C/C++', 'C/C++'),
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('Web(HTML,CSS,JavaScript)', 'Web(HTML,CSS,JavaScript)')
    )
    choice = MultiSelectField(choices=LANGUAGE_CHOICES, blank=True)

    def __str__(self):
        return self.name

    def get_name(request):
        user = member.objects.get(email=request.session['email'])
        return user.name

    def authenticate(useremail,password):
        user = member.objects.get(email=useremail)
        return check_password(password,user.password)

    def login(request):
        request.session['statue'] = 'login'
        request.session['email'] = request.POST['email']
        return request

    def logout(request):
        del request.session['statue']
        del request.session['email']
        return request
    def save(self, *args, **kwargs):
        self.password=make_password(self.password)
        super(member, self).save(*args, **kwargs)

class new(models.Model):
    title = models.CharField(max_length=20)
    contain = models.CharField(max_length=500)

    def __str__(self):
        return self.title
def generate_questionfiletest(self, filename):
    url = "static/question/%s/test.txt" % (self.title.replace(' ','_'))
    return url
def generate_questionfileans(self, filename):
    url = "static/question/%s/ans.txt" % (self.title.replace(' ','_'))
    return url
class problem(models.Model):
    title = models.CharField(max_length=30,unique=True)
    author = models.ForeignKey('member',to_field = 'name')
    context = models.TextField()
    test = models.FileField(upload_to=generate_questionfiletest,blank=True,null=True)
    ans = models.FileField(upload_to=generate_questionfileans)
    def __str__(self):
        return self.title

def generate_submissionfilename(self, filename):
    url = "static/submission/%s/%s/%s/" % (self.member.name,self.problem.id,datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    return url
class submission(models.Model):
    member = models.ForeignKey('member',to_field = 'name')    
    problem = models.ForeignKey('problem',to_field = 'title')
    status = models.CharField(max_length=20,default='waiting')
    lang = models.CharField(max_length=15,default='')
    code = models.FileField(upload_to=generate_submissionfilename)
    def __str__(self):
        return str(self.id)
