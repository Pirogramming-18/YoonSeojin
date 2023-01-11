from django.shortcuts import render

#요청(Request)를 넘겨받아 
#render 메서드를 호출
#받은 blog/post_list.html 템플릿을 보여준다
def post_list(request):
    return render(request, 'blog/post_list.html', {})

