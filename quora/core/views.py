from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from .models import User
from questans.models import Questions, Answers
from .forms import LoginForm, RegisterForm, QuestionForm, AnswerForm
from django.template import RequestContext


class DashboardView(FormView):

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            ques_obj = Questions.objects.all()
            content['form'] =QuestionForm
            content['userdetail'] = user
            content['questions'] = ques_obj
            #ans_obj = Answers.objects.filter(question=ques_obj[0])
            #content['answers'] = ans_obj
            return render(request, 'dashboard.html', content)
        else:
            return redirect(reverse('login-view'))
    @method_decorator(csrf_exempt)        
    def post(self, request):
        content = {}
        form = QuestionForm(request.POST, request.FILES or None)    
        if form.is_valid():
          save_i=form.save(commit=False)
          save_i.user=request.user
          print(save_i)
          save_i.save()
        return redirect(reverse('dashboard-view'))
       
class RegisterView(FormView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.password = make_password(form.cleaned_data['password'])
            save_it.save()
            login(request, save_it)
            return redirect(reverse('dashboard-view'))
        else:
            print("Form invalid")
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)


class LoginView(FormView):

    
    

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        content['form'] = LoginForm
        if request.user.is_authenticated:
            return redirect(reverse('dashboard-view'))
        return render(request, 'login.html', content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(username=username)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render_to_response('login.html', content)


class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class AnswerView(FormView):

    def get(self, request, question_id):
        content = {}
        question=Questions.objects.get(id=question_id)
        content['question'] = question
        answers=Answers.objects.filter(question=question)
        content['answers'] = answers
        content['answerform'] = AnswerForm
        return render(request,'answer.html', content)

   
    def post(self,request,question_id):
        question = Questions.objects.get(id = question_id)
        answerForm = AnswerForm(request.POST)
        answer = answerForm.save(commit = False)
        answer.user = request.user
        answer.question = question
        answer.save()

        return HttpResponseRedirect('/core/answers/'+str(question_id))






