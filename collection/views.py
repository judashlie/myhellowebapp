from django.shortcuts import render, redirect
from collection.forms import ProblemForm
from collection.models import Problem
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
	# defining the variable
	problems = Problem.objects.all()
	# passing the variable to the view
	return render(request, 'index.html', {
		'problems': problems,
		})

def problem_detail(request, slug):
	# grab the object
	problem = Problem.objects.get(slug=slug)

	# pass to the template
	return render(request, 'problems/problem_detail.html',{
		'problem': problem,
		})

@login_required
def edit_problem(request, slug):
	# grab the object
	problem = Problem.objects.get(slug=slug)

	# make sure the logged in user is the owner of the object
	if problem.user != request.user:
		raise Http404

	# set the form
	form_class = ProblemForm

	# if coming from a submitted form
	if request.method == 'POST':
		# grab the data from the submitted form and apply to the form
		form = form_class(data=request.POST, instance=problem)
		if form.is_valid():
			# save the new data
			form.save()
			return redirect('problem_detail', slug=problem.slug)
	# otherwise just create the form
	else:
		form = form_class(instance=problem)

	# and render the template
	return render(request, 'problems/edit_problem.html', {
		'problem': problem,
		'form': form,
	})

def create_problem(request):
	form_class = ProblemForm
	# if coming from a submitted form, do this
	if request.method == 'POST':
		# grab data from the submitted form and apply to the form
		form = form_class(request.POST)
		if form.is_valid():
			# create an instance, but don't save yet
			problem = form.save(commit=False)
			# set additional details
			problem.user = request.user
			problem.slug = slugify(problem.name)
			# save the object
			problem.save()
			# redirect to newly created problem
			return redirect('problem_detail', slug=problem.slug)
		# otherwise just create the form
	else:
		form = form_class()

	return render(request, 'problems/create_problem.html', {
		'form': form,
		})
