# README



### backend 실행

##### 가상환경 설치 방법

```python 
python -m venv venv
```

##### 가상환경 들어가는  법

```python 
source venv/Scripts/activate
```

##### 가상환경 끄는법

```python 
deactivate
```

##### 패키지 다운로드

```python 
pip install -r requirements.txt
```



##### db tags 저장

```python
python manage.py loaddata data/tags.json 
```



### 데이터 추출

##### dumpdata

> 데이터 저장

```python
python manage.py dumpdata --natural-foreign --natural-primary --exclude contenttypes --exclude auth.permission --exclude admin.logentry --exclude sessions.session --indent 4 > {파일명}
```



> 저장할때 한글이 깨지는 인코딩 에러가 발생했다 그래서 notepad++ 이라는 프로그램에서
> 
> Encoding -> Convert to utf-8로 다시 인코딩후 저장하니까 됬다ㅎㅎㅎㅎ



##### loaddata

> 데이터 로드

```python
python manage.py loaddata {파일명}
```