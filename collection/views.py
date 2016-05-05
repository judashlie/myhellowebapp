from django.shortcuts import render
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
