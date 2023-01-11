from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post #models.py에 정의된 모델 가져오기


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