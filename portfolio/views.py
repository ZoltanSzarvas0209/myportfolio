from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Project
from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.

def portfolio(request):
    """ A view to show the portfolio page """
    return render(request, 'portfolio/portfolio.html')

def about(request):
    """ A view to show the about page """
    return render(request, 'portfolio/about.html')

def tech(request):
    """ A view to show the technologies page """
    return render(request, 'portfolio/tech.html')

def projects(request):
    """ A view to show the projects page with projects data """

    projects = Project.objects.all()
    comment_forms = {project.id: CommentForm() for project in projects}  # Dictionary of forms per project

    if request.method == "POST":
        project_id = request.POST.get("project_id")  # Get project ID from form
        project = get_object_or_404(Project, id=project_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('projects')

    return render(request, 'portfolio/projects.html', {
        'projects': projects,
        'comment_forms': comment_forms  # Pass the dictionary to template
    })

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return HttpResponseForbidden("You are not allowed to edit this comment.")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('projects')  # Redirect to projects
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    comment.delete()
    return redirect('projects')  # Redirect to projects