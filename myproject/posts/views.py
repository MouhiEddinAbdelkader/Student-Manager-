from django.shortcuts import render, redirect, get_object_or_404
from .models import  Poste, Stage, Logement, LikePost, EvenClub
from users.models import Profile
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django. contrib import messages
from django.views.generic.edit import  DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import StageForm
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.contrib.auth.models import User, auth
from django.utils.decorators import method_decorator





# Create your views here.

def Postes_Listes(request):
    stages = Stage.objects.all()
    logements = Logement.objects.all()
    evenclub = EvenClub.objects.all()
    return render(request, 'posts/postes_list.html', {'stages': stages, 'logements': logements, 'evenclub': evenclub})

def Stages_list(request):
    stages = Stage.objects.all()
    return render(request, 'posts/Stages_list.html', { 'stages': stages })    

def EvenClub_list(request):
    evenClub = EvenClub.objects.all()
    return render(request, 'posts/even_club_list.html', {'evenClub': evenClub})

def Poste_page(request, slug):
    post = Poste.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post' : post} )

@login_required
def edit_stage(request, id):
    stage = get_object_or_404(Stage, id=id)
    if request.method == 'GET':
        context = {'form': forms.StageForm(instance=stage), 'id' : id}
        return render(request,'posts/stage_EditForm.html',context)
    elif request.method == 'POST':
        form = forms.StageForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect("stages_list")
    else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'posts/stage_EditForm.html',{'form':form})

@method_decorator(login_required, name='dispatch')
def evenClub_update_view(request, id):
    evenclub = get_object_or_404(EvenClub, id=id)
    
    if request.method == "GET":
        form = forms.CreateEvenClub(instance=evenclub)
        context = {'form': form, 'id': id}
        return render(request, 'posts/even_club_update_view.html', context)
    
    elif request.method == 'POST':
        form =forms. CreateEvenClub(request.POST, instance=evenclub)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect("posts:listes")
        else:
            messages.error(request, 'Please correct the following errors:')
    
    context = {'form': form, 'id': id}
    return render(request, 'posts/even_club_update_view.html', context)

    
@method_decorator(login_required, name='dispatch')
class StageDeleteView(DeleteView):
    model = Stage
    template_name = 'posts\stage_delete.html'
    success_url = reverse_lazy('posts:listes')
@method_decorator(login_required, name='dispatch')
class EvenClubDeleteView(DeleteView):
    model = EvenClub
    template_name = 'posts\evenclub_delete.html'
    success_url = reverse_lazy('posts:listes')


    
@method_decorator(login_required, name='dispatch')
class CreerStage(CreateView):
   model = Stage
   template_name = 'posts/stage_form.html'
   form_class = StageForm   
   success_url = reverse_lazy('posts:listes')
   
   
   
   
   
@method_decorator(login_required, name='dispatch')
class creerEvenClub(CreateView):
    model = EvenClub
    template_name = 'posts/evenClubForm.html'
    form_class = forms.CreateEvenClub
    success_url = reverse_lazy('posts:listes')




    

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:listes')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form ' : form })

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@require_GET
@login_required
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    
    post = Poste.objects.get(id=post_id)
    
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()
    
    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes += 1
        liked = True
    else:
        like_filter.delete()
        post.no_of_likes -= 1
        liked = False
    
    post.save()
    
    return JsonResponse({'no_of_likes': post.no_of_likes, 'liked': liked})


# def search(request):
#     user_Object = User.Objects.get(username=request.user.username)
#     user_profile = Profile.objects.get(user=user_object)
    
#     user_following_list = []
#     feed = []
    
#     user_following = FollowersCount.objects.filter(follower=request.user.username)
