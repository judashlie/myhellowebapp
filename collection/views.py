from django.shortcuts import render, redirect
from collection.forms import ProblemForm
from collection.models import Problem

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

def edit_problem(request, slug):
	# grab the object
	problem = Problem.objects.get(slug=slug)
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
