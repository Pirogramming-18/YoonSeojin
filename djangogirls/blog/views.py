from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post #models.py에 정의된 모델 가져오기
from .forms import PostForm

#요청(Request = 사용자가 요청하는 것)를 넘겨받아 
#render 메서드를 호출
#받은 blog/post_list.html 템플릿을 보여준다
#템플릿을 사용하기 위해 매개변수 posts추가
def post_list(request):
    #posts변수는 쿼리셋의 이름
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #작성자 추가 후 저장하기 ㄷ위해 바로 Post모델에 저장하지 않게 함
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #변경사항을 유지, 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})