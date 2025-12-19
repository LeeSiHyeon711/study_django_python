# Django Web Programming 실습 프로젝트

Django 학습 교재를 기반으로 한 웹 애플리케이션 실습 프로젝트입니다.

## 📋 프로젝트 개요

이 프로젝트는 Django 프레임워크를 사용하여 구현된 웹 애플리케이션으로, 블로그, 북마크, 사진 갤러리 기능을 제공합니다.

## 🛠 기술 스택

- **Backend**: Django 6.0
- **Database**: MariaDB (MySQL 호환)
- **Python**: 3.14
- **Frontend**: Bootstrap 5.3.8
- **기타 라이브러리**:
  - django-taggit: 태그 기능
  - Pillow: 이미지 처리
  - PyMySQL: MySQL/MariaDB 연결

## 📁 프로젝트 구조

```
study_django_python/
├── project/                    # Django 프로젝트 루트
│   ├── manage.py              # Django 관리 스크립트
│   ├── mysite/                # 프로젝트 설정 디렉토리
│   │   ├── __init__.py
│   │   ├── settings.py        # 프로젝트 설정
│   │   ├── urls.py            # 메인 URL 설정
│   │   ├── views.py           # 홈 뷰
│   │   ├── wsgi.py            # WSGI 설정
│   │   └── asgi.py            # ASGI 설정
│   │
│   ├── bookmark/              # 북마크 앱
│   │   ├── models.py          # Bookmark 모델 (title, url)
│   │   ├── views.py           # ListView, DetailView
│   │   ├── urls.py            # 북마크 URL 라우팅
│   │   ├── admin.py           # Admin 설정
│   │   └── templates/
│   │       └── bookmark/
│   │           ├── bookmark_list.html
│   │           └── bookmark_detail.html
│   │
│   ├── blog/                  # 블로그 앱
│   │   ├── models.py          # Post 모델 (제목, 내용, 태그 등)
│   │   ├── views.py           # 다양한 ArchiveView 구현
│   │   ├── urls.py            # 블로그 URL 라우팅
│   │   ├── forms.py           # 검색 폼
│   │   ├── admin.py           # Admin 설정
│   │   └── templates/
│   │       ├── blog/
│   │       │   ├── post_all.html          # 전체 포스트 목록
│   │       │   ├── post_detail.html       # 포스트 상세
│   │       │   ├── post_archive.html       # 아카이브 인덱스
│   │       │   ├── post_archive_year.html  # 연도별 아카이브
│   │       │   ├── post_archive_month.html # 월별 아카이브
│   │       │   ├── post_archive_day.html   # 일별 아카이브
│   │       │   └── post_search.html         # 검색 결과
│   │       └── taggit/
│   │           ├── taggit_cloud.html       # 태그 클라우드
│   │           └── taggit_post_list.html  # 태그별 포스트 목록
│   │
│   ├── photo/                 # 사진 갤러리 앱
│   │   ├── models.py          # Album, Photo 모델
│   │   ├── views.py           # Album/Photo 뷰
│   │   ├── urls.py            # 사진 갤러리 URL 라우팅
│   │   ├── fields.py          # ThumbnailImageField 커스텀 필드
│   │   ├── admin.py           # Admin 설정
│   │   └── templates/
│   │       └── photo/
│   │           ├── album_list.html    # 앨범 목록
│   │           ├── album_detail.html  # 앨범 상세
│   │           └── photo_detail.html  # 사진 상세
│   │
│   ├── templates/             # 공통 템플릿
│   │   ├── base.html          # 기본 레이아웃 (네비게이션 바 포함)
│   │   └── home.html          # 홈 페이지
│   │
│   ├── static/                # 정적 파일
│   │   └── img/               # 이미지 파일
│   │
│   └── media/                  # 업로드된 미디어 파일
│       └── photo/              # 업로드된 사진들
│
└── requirements.txt            # Python 패키지 의존성
```

## 🚀 설치 및 실행 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd study_django_python
```

### 2. 가상 환경 생성 및 활성화

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 또는
.venv\Scripts\activate  # Windows
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 설정

#### MariaDB 설치 (Homebrew 사용)

```bash
brew install mariadb
brew services start mariadb
```

#### 데이터베이스 생성

```bash
mysql -u root -p
```

```sql
CREATE DATABASE mysite CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';
FLUSH PRIVILEGES;
exit;
```

### 5. 환경 설정

`project/mysite/settings.py`에서 데이터베이스 설정 확인:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. 마이그레이션 실행

```bash
cd project
python manage.py migrate
```

### 7. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 8. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000` 접속

## 📱 주요 기능

### 1. 북마크 (Bookmark)
- URL 저장 및 관리
- 북마크 목록 및 상세 보기

### 2. 블로그 (Blog)
- 포스트 작성, 수정, 삭제
- 포스트 목록 (페이지네이션)
- 포스트 상세 보기
- 날짜별 아카이브 (연도/월/일)
- 태그 시스템
  - 태그 클라우드
  - 태그별 포스트 필터링
- 검색 기능 (제목, 설명, 내용)

### 3. 사진 갤러리 (Photo)
- 앨범 생성 및 관리
- 사진 업로드
- 자동 썸네일 생성 (200x200px)
- 앨범별 사진 그룹화

## 🔧 주요 설정

### INSTALLED_APPS
- `bookmark`: 북마크 앱
- `blog`: 블로그 앱
- `photo`: 사진 갤러리 앱
- `taggit`: 태그 기능
- `taggit_templatetags2`: 태그 템플릿 태그

### 데이터베이스
- MariaDB 사용
- PyMySQL을 통한 연결

### 미디어 파일
- 업로드 경로: `media/photo/%Y/%m`
- 썸네일 자동 생성

## 📝 학습 내용

이 프로젝트를 통해 학습한 주요 내용:

1. **Django 기본 구조**
   - 프로젝트와 앱의 개념
   - MVT 패턴

2. **모델 (Models)**
   - 모델 정의 및 필드 타입
   - 관계 설정 (ForeignKey)
   - 커스텀 필드 생성

3. **뷰 (Views)**
   - Class-based Views
   - ListView, DetailView
   - ArchiveView (Year, Month, Day)

4. **템플릿 (Templates)**
   - 템플릿 상속
   - 템플릿 태그와 필터
   - Bootstrap을 활용한 UI

5. **URL 라우팅**
   - URL 패턴 정의
   - 네임스페이스 사용

6. **Admin 인터페이스**
   - 모델 등록
   - Inline 편집

7. **태그 시스템**
   - django-taggit 활용
   - 태그 클라우드 구현

8. **이미지 처리**
   - Pillow를 활용한 썸네일 생성
   - 커스텀 이미지 필드

## 📚 참고 자료

- [Django 공식 문서](https://docs.djangoproject.com/)
- [Bootstrap 문서](https://getbootstrap.com/)
- [django-taggit 문서](https://django-taggit.readthedocs.io/)

## 📄 라이선스

이 프로젝트는 학습 목적으로 작성되었습니다.
