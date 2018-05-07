from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from final.utils import classify

# Create your views here.
def index(request):
	template_name = 'final/form.html'
	# return HttpResponse('Hello Bhai')
	context = {}
	if request.GET:
		print('Get Method')
	if request.POST:
		print('Post Method')
		messege = request.POST.get('exampleInputMessege').strip()

		if not messege:
			print("No messege")
			return render(request, template_name, context)
		else:
			print("messege")
		result = classify(messege, show_details=False)
		# print(result[0][1]*100)
		# print(type(result[0][1]))
		print(result)
		if not result:
			#print("Not Found")
			context = {
			'disease': 'Not Found',
			'accuracy': 0,
		}
		else:
			context = {
			'disease': result[0][0],
			'accuracy': "{:.2f}".format(result[0][1]*100),
		}

		# return HttpResponseRedirect('/result')
		return render(request, 'final/result.html', context)
	return render(request, template_name, context)



def result(request):
	template_name = 'final/result.html'
	context = {}
	return render(request,template_name,context)