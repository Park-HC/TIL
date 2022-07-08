# Admin Site

## Automatic admin interface

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록, 관리
- django.contrib.auth 모듈에서 제공됨
- record 생성 여부 확인에 매우 유용
- 직접 record 생성, 삽입, 삭제 가능



## admin 생성

```python
$ python manage.py createsuperuser
```

- 관리자 계정 생성하고 서버 실행 후 `/admin` 페이지로 가 관리자 로그인
  - 계정만 만든 경우 관리자 화면에서 아무 것도 보이지 않음

```python
from .models import Article
admin.site.register(Article)
```

- `admin.py`에 Model을 등록해서 조작 가능

```python
class ArticleAdmin(admin, ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'modifiec_at',)
admin.stie.register(Article, ArticleAdmin)    
```

- `list_display`: `models.py`에 정의한 각각의 속성들의 값이 admin 페이지 출력되도록 설정