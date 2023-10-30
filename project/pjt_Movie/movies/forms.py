from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'title form-control',
                'placeholder': 'ex) 기생충',
                'maxlength': 20,
            }
        )
    )
    description = forms.CharField(
        label='설명',
        widget=forms.Textarea(
            attrs={
                'class': 'description form-control',
                'placeholder': 'ex) 전원백수로 살 길 막막하지만 사이는 좋은 기택(송강호) 가족. 장남 기우(최우식)에게...',
                'rows': 5,
                'cols': 50,
                'maxlength': 200,
            }
        ),
        error_messages={
            'required': 'Please enter your content!!!'
        }
    )

    PICK_Comedy = '코미디'
    PICK_Fantasy = '판타지'
    PICK_Romance = '로맨스'
    PICK_Action = '액션'
    PICK_horror = '공포'
    PICK_Etc = '기타'

    PICKS = [
        (PICK_Comedy, '코미디'),
        (PICK_Fantasy, '판타지'),
        (PICK_Romance, '로맨스'),
        (PICK_Action , '액션'),
        (PICK_horror, '공포'),
        (PICK_Etc, '기타'),
    ]
    genre = forms.ChoiceField(choices=PICKS, widget=forms.Select(), label='장르')

    score = forms.DecimalField(
        label='평점',
        widget=forms.NumberInput(
            attrs={
                'class': 'score form-control',
                'min': '0',
                'max': '5',
                'step': '1',
            }
        ),
        min_value=0,
        max_value=5,
        decimal_places=0.5,
    )
    
    class Meta:
        model = Movie
        exclude = ('user', 'like_users')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
