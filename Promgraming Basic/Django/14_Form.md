# Form

## 개요

- Django의 유효성 검사 도구 중 하나
  - 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

- Form의 기능
  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML forms 생성
  - 클라이언트로부터 받은 데이터 수신 및 처리



## Form Class

- Form 내 field, filed 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러 메세지를 결정
- Django는 사용자의 데이터를 받을 때 해야할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여줌
- 어느 위치에 두어도 상관없지만 app폴더/forms.py에 작성하는 것이 일반적



## 사용법

### 선언하기

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```



### rendering options

- `<label>` & `<input>` 쌍에 대한 3가지 출력 옵션

1. `as_p()`
   - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링 됨
2. `as_ul()`
   - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링 됨
   - `<ul>` 태그는 직접 작성해야 함
3. `as_table()`
   - 각 필드가 테이블(`<table>` 태그) 행으로 감싸져서 렌더링 됨
   - `<table>` 태그는 직접 작성해야 함



### HTML input 요소 표현 방법

#### Form fields

- input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용 됨

#### Widgets

- 웹 페이지의 HTML input 요소 렌더링
- GET/POST 딕셔너리에서 데이터 추출
- widgets은 반드시 Form fields에 할당 됨



- Form fields는 유효성 검사 처리, widget은 단순 raw한 렌더링 처리



```python
from django import forms

class ArticleForm(forms.Form):
    REGION_A = "sl"
    REGION_B = "dj"
    REGION_C = "gj"
    REGION_D = "gm"
    REGION_E = "bu"
    REGIONS_CHOICES = [
        (REGION_A, "서울"),
        (REGION_B, "대전"),
        (REGION_C, "광주"),
        (REGION_D, "구미"),
        (REGION_E, "부산"),
    ]
    
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceFeild(choices=REGION_CHOICES, widget=forms.Select())
```



```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
	class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            })
        }
        
        
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    	label='제목',
        widget=forms.TextInput(
        	attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    
	class Meta:
        model = Article
        fields = '__all__'
# 두 번째 방법 권장
```



# ModelForm

## 개요

- Model에 정의한 필드를 유저로 부터 입력 받기 위해 Form에서 Model 필드를 재정의하는 행위가 중복 될 수 있음
- Django는 Model을 통해 Form Class를 만들 수 있는 ModelForm이라는 Helper를 제공



## ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 Helper
- 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능



## Meta class

- Model의 정보를 작성하는 곳
- ModelForm을 사용할 경우 사용할 모델이 있어야 하는데 Meta Class가 이를 구성함
  - 해당 Model에 정의한 field 정보를 Form에 적용하기 위함



### Inner Class(Nested Class)

- 클래스 내에 선언된 다른 클래스
- 관련 클래스를 함께 그룹화 하여 가독성 및 프로그램 유지 관리를 지원 (논리적으로 묶어서 표현)
- 외부에서 내부 클래스에 접근할 수 없으므로 코드의 복잡성을 줄일 수 있음



### Meta 데이터

- 데이터에 대한 데이터
- ex - 사진 촬영 - 사진 데이터 - 사진의 메타 데이터(촬영 시각, 렌즈, 조리개 값 등)



## 예시

### Create(form)

```python
# articles/views.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valide():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```



### DELETE(Modelform)

```python
# views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

```html
<!-- detail.html -->

<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```





## 사용법

### 선언하기

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ( 'title', )  # exclude와 fields는 동시에 사용할 수 없음!
```



### is_valid() method

- 유효성 검사를 실행하고, 데이터가 유효하지 여부를 boolean으로 반환

#### 유효성 검사

- 요청한 데이터가 특정 조건에 충족하는지 확인하는 작업
- 데이터베이스 각 필드 조건에 올바르지 않은 데이터가 서버로 전송되거나 저장되지 않도록 하는 것



### The save() method

- Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장
- ModelForm의 하위(sub) 클래스는 기존 모델 인스터스를 키워드 인자 instance로 받아 들일 수 있음
  - 이것이 제공되면 save()는 해당 인스턴스를 수정(Update)
  - 제공되지 않는 경우 save()는 지정된 모델의 새 인스턴스를 만듦(Create)
- Form의 유효성이 확인되지 않은 경우 save()를 호출하면 form.errors를 확인하여 에러 확인 가능



## Form과 ModelForm 비교

### Form

- 어떤 Model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성
- cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야 함
- Model에 연관되지 않은 데이터를 받을 때 사용



### ModelForm

- Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
- 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save() 호출 가능



# 수동 Form 작성법

1. Rendering fields manually
2. Looping over the form's fields