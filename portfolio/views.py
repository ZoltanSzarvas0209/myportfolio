from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Project
from comments.models import Comment
from comments.forms import CommentForm
from django.contrib import messages


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
    # Dictionary of forms per project
    comment_forms = {project.id: CommentForm() for project in projects}

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
        return HttpResponseForbidden("You're not allowed to edit this comment")

    projects = Project.objects.all()  # Load all projects
    # Default forms for new comments
    comment_forms = {project.id: CommentForm() for project in projects}

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            # Reload the projects page after saving
            return redirect('projects')
    else:
        # Pre-fill form with existing comment
        form = CommentForm(instance=comment)

    return render(request, 'portfolio/projects.html', {
        'projects': projects,
        'comment_forms': comment_forms,  # Keep normal comment forms
        'edit_comment_form': form,  # Form for the comment being edited
        'edit_comment_id': comment.id  # ID to identify the comment edited
    })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        messages.warning(request, ("You're not allowed to delete comment!"))

    comment.delete()
    return redirect('projects')  # Redirect to projects
