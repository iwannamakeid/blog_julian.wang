from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .form import BlogPost
# Create your views here.

def home(request):
    blogs=Blog.objects
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request):
    # new에서 입력받은 내용을 데이터베이스에 넣어주기
        blog = Blog()
        blog.title = request.GET['title']
        blog.body = request.GET['body']        
        blog.pub_date = timezone.datetime.now()
        blog.save() #데이터베이스에 저장하라는 뜻. 객체.delete():데베로부터 이 객체 지우삼
    
        return redirect('/blog/'+str(blog.id))
  
    # redirect: 위 작업들 처리 후 옆의 url로 넘겨라 -> 완전히 관계없는 주소를 실행 가능.
    # render: 세번째 인자로 키값을 가짐, 따라서 함수 안에서 다룬 내용을 html상에서 정리, 보여줄 때 사용

def blogpost(request):
    if request.method == 'POST':
        # POST방식으로 요청이 들어왔을 때 실행할 코드 - form에 입력받은 데이터를 저장하기
        # POST: 입력된 내용을 처리하는 기능
        form = BlogPost(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')

    else:
          # GET방식으로 요청이 들어왔을 때 실행할 코드 - form을 보여주기
            #빈 페이지 띄워주는 기능 ->GET   
        form =BlogPost()
        return render( request, 'new.html', {'form':form})