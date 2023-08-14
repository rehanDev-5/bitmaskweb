from unicodedata import name
from django.shortcuts import render,redirect
from .models import Blog, UserQuery

# Create your views here.
def index(request):
    context = {}
    context['blogs'] = Blog.objects.all()[:3]
    for i in context['blogs']:
        print(i.img)

    if request.method == "POST":
        u_name = request.POST.get('uname')
        u_mail = request.POST.get('umail')
        u_msg = request.POST.get('umsg')
        u_pno = request.POST.get('upno')
        print(u_name)
        obj = UserQuery.objects.create(name=u_name,email=u_mail,pno=u_pno,msg=u_msg)
        obj.save()
        return redirect('/#contact')
    return render(request, 'index.html',context)

def blogs_avail(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'blogs.html', context)

def blog_page(request, pk):
    b_obj = Blog.objects.get(pk=pk)
    return render(request, 'blogpage.html',{'blog':b_obj})


def error_404(request, exception):
    data = {}
    data['exce'] = exception
    return render(request, 'herror/404.html',data)