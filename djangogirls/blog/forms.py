# from django import forms
# from .models import Post

# #우리가 만들 폼의 이름 / modelform임을 알려줌
# class PostForm(forms.ModelForm) :
#     #폼을 만들기 위해 어떤 모델이 쓰여야 하는지 알려주기 위함
#     class Meta:
#         Model = Post
#         #폼에 필드 넣기
#         fields = ('title', 'text', )

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)