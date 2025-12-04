from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from accounts.models import Accounts
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from .models import Repository
from django.contrib import messages
from django.contrib.auth.models import User





@login_required
@require_POST
def create_repo(request):
    filename = request.POST.get('filename', '').strip()
    filetype = request.POST.get('filetype', '').strip()  # e.g. ".js"
    description = request.POST.get('description', '').strip()
    privacy = request.POST.get('privacy', 'private').strip()
    language_mode = request.POST.get('language_mode', 'text').strip()

    # validation
    if not filename:
        return JsonResponse({'status': False, 'message': 'Filename required'}, status=400)

    word_count = len([w for w in description.split() if w.strip()])
    if word_count < 20:
        return JsonResponse({'status': False, 'message': 'Description must be at least 20 words'}, status=400)

    full_name = filename + (filetype or '')
    repo = Repository.objects.create(
        user=request.user,
        repo_name=full_name,
        repo_content='',
        type=(filetype or '').replace('.', ''),
        repo_visiblity=privacy,
        repo_description=description,
        language_mode=language_mode
    )

    return JsonResponse({
        'status': True,
        'message': 'Repository created successfully',
        'data': {
            'id': repo.id,
            'repo_name': repo.repo_name,
            'type': repo.type,
            'language_mode': repo.language_mode
        }
    })


@login_required
def load_repo(request, id):
    repo = get_object_or_404(Repository, id=id, user=request.user)
    return JsonResponse({
        'status': True,
        'data': {
            'id': repo.id,
            'repo_name': repo.repo_name,
            'repo_content': repo.repo_content or '',
            'repo_description': repo.repo_description or '',
            'type': repo.type or '',
            'language_mode': repo.language_mode or 'text',
            'repo_visiblity': repo.repo_visiblity or 'private'   # ADDED
        }
    })


@login_required
@require_POST
def save_repo(request, id):
    repo = get_object_or_404(Repository, id=id, user=request.user)
    content = request.POST.get('content', None)
    description = request.POST.get('description', None)
    language_mode = request.POST.get('language_mode', None)

    if content is None:
        return JsonResponse({'status': False, 'message': 'No content provided'}, status=400)

    repo.repo_content = content
    if description is not None:
        repo.repo_description = description
    if language_mode:
        repo.language_mode = language_mode
    repo.save()

    return JsonResponse({'status': True, 'message': 'Saved successfully'})


@login_required
@require_POST
def delete_repo(request, id):
    repo = get_object_or_404(Repository, id=id, user=request.user)
    repo.delete()
    return JsonResponse({'status': True, 'message': 'Deleted'})




# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def auth(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            # Process login data
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('auth')
                
        elif action == 'signup':
            # Process signup (only after email verification)
            email_verified = request.POST.get('email_verified')
            
            if email_verified == 'true':
                full_name = request.POST.get('full_name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                
                # Check if user already exists
                if User.objects.filter(email=email).exists():
                    return redirect('auth')
                
                # Create new user
                auth_user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )
                auth_user.first_name = full_name.split()[0] if full_name else ''
                auth_user.last_name = ' '.join(full_name.split()[1:]) if len(full_name.split()) > 1 else ''
                auth_user.save()
                
                # Log the user in
                logout(request)
                login(request, auth_user, backend='Codesync.custom_backend.CustomBackend')
                
                return redirect('dashboard')
            else:
                return redirect('auth')
    
    # This handles GET requests - must be at the same indentation level as "if request.method == 'POST':"
    return render(request, 'auth.html')



def billing(request):
    return render(request, 'billing.html')

def change_pass(request):
    return render(request, 'change-password.html')

@login_required
def dashboard(request):
    repo_count = Repository.objects.filter(user=request.user).count()
    repos = Repository.objects.filter(user=request.user).order_by('-created_at')[:3]
    return render(request, 'dashboard.html', {'repos': repos,"repo_count": repo_count})

@login_required
def pulls(request):
    return render(request, 'pulls.html')

@login_required
def repo(request):
    repos = Repository.objects.filter(user=request.user).order_by('-created_at')
    first_repo = repos.first()
    repo_visiblity = first_repo.repo_visiblity if first_repo else 'private'
    context = {
        'repos': repos,
        'repo_visiblity': repo_visiblity,   # ADDED for template
    }
    return render(request, 'repo.html', context)

def settings(request):
   
    repos = Repository.objects.filter(user=request.user).order_by('-created_at')[:3]
    return render(request, 'settings.html', {'repos': repos,})



def api(request):
    return render(request, 'api.html')

def blog(request):
    return render(request, 'blog.html')


def career(request):
    return render(request, 'careers.html')

def community(request):
    return render(request, 'community.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

@login_required
def change_pass(request):
    return render(request, 'change_pass.html')

def security(request):
    return render(request, 'security.html')

def policy(request):
    return render(request, 'privacy.html')

def help_center(request):
    return render(request, 'help.html')

def system_status(request):
    return render(request, 'status.html')

def terms_condition(request):
    return render(request, 'terms.html')

@login_required
def logouts(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
    #     data=Accounts(full_name=full_name,email=email,password=password)
    #     data.save()
    #     return redirect('/dashboard')
    # return render(request, 'signup.html')


# @login_required
# def Repository(request):
#     if request.method == 'POST':
#         repo_name = request.POST.get('repo_name')
#         repo_content = request.POST.get('repo_content')
#         user = request.user  # Assuming the user is logged in

#         # Create and save the new repository
#         new_repo = Repository(repo_name=repo_name, repo_content=repo_content, user=user)
#         new_repo.save()

#         return redirect('dashboard')  # Redirect to a relevant page after creation

#     return render(request, 'create_repo.html')  # Render a form for creating a repository






@login_required
def team(request):
    return render(request, 'team.html')
