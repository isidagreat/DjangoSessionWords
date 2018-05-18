from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, "index.html")

def process(request):
	if 'word' not in request.session:
		request.session['word'] = []
		temp_list = request.session['word']
		temp_list.append({'words': request.POST['newword'], 'color': request.POST['color'], 'bigfont': request.POST['bigg'] })
		request.session['word'] = temp_list
		
	else:
		temp_list = request.session['word']
		temp_list.append({'words': request.POST['newword'], 'color': request.POST['color'], 'bigfont': request.POST['bigg'] })
		request.session['word'] = temp_list
		
		print(request.session['word'])
	return redirect(index)

def clear(request):
	request.session.clear()
	return redirect(index)
