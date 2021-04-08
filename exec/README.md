# 알고가

![로고](/uploads/9db12f1663e34251619fde2e1db60423/로고.png)

알고리즘을 알고가! 의 의미를 갖고있습니다.

빅데이터를 기반으로 하여 사용자가 푼 알고리즘 문제를 기반으로 문제를 추천해주고 관리하며 **사용자의 알고리즘 역량**을 키울 수 있는 서비스입니다. 



### 🌴팀명 - 알로하 

알고리즘의 세계로 ~ 알로하! 의미를 갖고 있습니다.🌱 🌏🌴⛺⛵ 



### 🌴알로하 팀원소개

![팀원소개](/uploads/3f80bc5597b75d5286ca47b9cad3a839/팀원소개.png)

️**프론트엔드**  

1. **이동희**  - [@Donghee-L](https://github.com/Donghee-L)

2. **박철완**  - [@Parking9](https://github.com/Parking9)

️**백엔드**  

1. **최은선**  - [@esun1903](https://github.com/esun1903)

2. **표기동**  - [@pyoki32](https://github.com/pyoki32)


️**데이터분석**  

1. **권영일** - [@KwonYI](https://github.com/KwonYI)

### 🌴기간

2021.03.08 - 2021.04.09



### ✔ 기획배경

![기획배경](/uploads/6028abce703287cedf301642c5fb4781/기획배경.PNG)

다양한 알고리즘 사이트들이 있지만 자신이 어떠한 부분이 부족한지 어떤 문제를 풀어야할지 모를때가 많습니다. 이를 위해 알고가에서는 사용자가 부족한 알고리즘 분야를 알려주고 문제를 추천해주어알고리즘의 역량을 기를 수 있습니다. 



### ✔ 주요기능 및 서비스

![주요기능](/uploads/1c4a820ff6ba45bab9a9347a7fd8da5b/주요기능.PNG)


### ✔ ERD 설계 

![erd](/uploads/91d432142fa48e9ccc8496e3526205f6/erd.png)

### ✔ 기술스택




### ⚙️ Install and Usage

# 🌴알고가 배포 과정

## 📘1. EC2 접속 & 도커 이미지 생성

  **1.1 파이썬 설치 (알고가 서비스 기준)**
       Python 3.6.1

 
  **1.2 도커 설치**
       Docker  20.10.5

  **1.3** **MySQL Docker 이미지 다운로드**

```jsx
$ docker pull mysql:8.0.17
```

  **1.4 Docker 이미지 확인**

```jsx
$ docker images
```

**1.5 한글이 깨지지 않도록 설정하려면 아래 인자값을 넣어주어야 한다.**

```jsx
$  --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

**1.6 Docker MySQL 컨테이너 생성 및 실행**

```jsx
$ docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ssafy1234 --name ssafy-mysql -v /Users/ssafy/datadir:/var/lib/mysql mysql:8.0.17 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

MYSQL_ROOT_PASSWORD = ssafy1234
mysql -ssafy
```

**1.7 MySQL 컨테이너 bash 쉘 접속**
docker exec 명령을 사용하여 docker 컨테이너에 접근한 다음 MySQL에 로그인한다.

```jsx
$ docker exec -it ssafy-mysql bash
$ root@f3aasdasdasd8:/#mysql -u root -p
```

mysql>

데이터베이스와 사용자를 생성하고 (컨테이너 내에서) MySQL에서 권한을 부여한다.
ssafy 사용자를 생성하고, 모든 권한을 부여한다.
변경된 권한 적용
중요 : 컨테이너 외부에서 MySQL에 로그인도 가능해야 하므로 ssafy@localhost에서 localhost 대신 %를 사용한다.
```jsx
mysql> CREATE USER 'ssafy'@'%' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'ssafy'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit
```


## 📗2. Git

2-1. git install  브랜치 master 기준

2-2. git clone  해당 서비스 주소 

---

## 📒3. EC2 접속 (1과 동일한 화면에서 진행하면 됨)

  cd s04p23a302

---

## 📕4. Frontend 배포

4-1. cd algoga-frontend

```jsx
cd algoga-frontend
```

4-2. npm install

```jsx
$ npm install
```

4-3. npm run serve    ----> 확인하는 명령어 

```jsx
$ npm run serve
```

4-4. npm run build    ——> dist 생성 

```jsx
$ npm run build
```

---

## 📕5. Backend 배포 및 가상환경 구축

 5-1. 

```jsx
$ cd algoga-backend
```

 5-2. my_settings.py 작성 [mysetting.py](http://mysetting.py/) 위치 algoga-backend/
```jsx
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'db-name',
'USER': 'xxxxx',
'PASSWORD':'xxxxx',
'HOST': 'xxxxxxx',
'PORT': '3306',
}
}

SECRET_KEY = 'xxxxxxx'

EMAIL = {
'EMAIL_BACKEND' : 'django.core.mail.backends.smtp.EmailBackend',
'EMAIL_USE_TLS' : True,
'EMAIL_PORT' : 587,
'EMAIL_HOST' : '[smtp.googlemail.com](http://smtp.googlemail.com/)',
'EMAIL_HOST_USER' : 'xxxxxx',
'EMAIL_HOST_PASSWORD' : 'xxxxxxx',
}

###########################AWS
AWS_ACCESS_KEY_ID = 'xxxxxxxX' # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = 'xxxxxxxxx' # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

###S3 Storages
AWS_STORAGE_BUCKET_NAME = 'xxxx' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%[s.amazonaws.com](http://s.amazonaws.com/)' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```
---

**xxxxx 자신의 알맞는 내용으로 넣기**


5-3. 가상환경 구축

```jsx
$ python3 -m venv env
```

5-4 . makemigrations,migrate,구동 확인

```jsx
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

algoga-backend/로 이동 

5-9. nginx설치
5-10. uwsgi 설치

5-11. sudo apt-get install nginx

```jsx
$ sudo apt-get install nginx
```

5-12. pip install uwsgi

```jsx
$ pip install uwsgi
```

5-13. vi algoga_uwsgi.ini

```jsx
$ vi algoga_uwsgi.ini
```
```jsx
[uwsgi]
chdir = /home/ubuntu/algoga1.0/s04p23a302/algoga-backend
module = backend.wsgi

socket = /home/ubuntu/algoga1.0/s04p23a302/algoga-backend/algoga.sock

socket = 127.0.0.1:8001

chmod-socket = 666
vacuum = true

#home = /home/jihun/.pyenv/versions/algoga-backend/
#virtualenv = /home/jihun/.pyenv/versions/algoga-backend/

daemonize = /home/ubuntu/algoga1.0/s04p23a302/algoga-backend/algoga_uwsgi.log

die-on-term = true
```
module : django 프로젝트를 생성하면 자동으로 생성되는 wsgi 파일을 지정한다.<br>
socket : socket 파일을 이용하는 경우 소켓이 생성될 위치와 함께 .sock 파일명을 입력한다. ip, port를 이용하고 싶은 경우 주석으로 처리된 부분과 같이 지정하면 된다.<br>
home, virtualenv : virtualenv를 이용하는 경우 가상 환경의 경로를 지정해줘야 한다.<br>
daemonize : 백그라운드로 실행 하도록 하는 설정을 하면서 로그가 저장될 파일 위치를 지정한다.<br>

가상환경 위에서 배포하시면 home,virtualenv 주석제거

5-14. $ uwsgi --ini algoga_uwsgi.ini

```jsx
 $ uwsgi --ini algoga_uwsgi.ini;
```

정상적으로 실행이 되면 memorist.sock 소켓 파일이 생성되고, 로그가 memorist_uwsgi.log에 기록된다.

5-15. algoga_uwsgi.log  // algoga.sock  생성됨

5-16. killall uwsgi; 백그라운드 에서 실행되는 백서버 죽이기

```jsx
$ killall uwsgi
```

5-17.  uwsgi --ini algoga_uwsgi.ini 백엔드서버 가동

```jsx
$ uwsgi --ini algoga_uwsgi.ini
```

5-18. sudo vim /etc/nginx/sites-enabled/default

```jsx
 sudo vim /etc/nginx/sites-enabled/default
```

nignx

5.19. frotend 경로 맞추기
5-20. backend reverse proxy 설정 추가

연결 과정
```jsx
server {
listen 80;
...
..


root /home/ubuntu/algoga1.2/s04p23a302/frontend/algoga-frontend/dist

location / {
	# First attempt to serve request as file, then
	# as directory, then fall back to displaying a 404.
	try_files $uri $uri/ =404;
}


     location /apps {

       	include uwsgi_params;
	uwsgi_pass unix:/home/ubuntu/algoga1.2/s04p23a302/backend/backend/algoga.sock;
	#backend sock 있던 위치

}
```




## 🌳6. Syntax 검사 및 Nginx 재시작 (배포과정 끝)

설정 변경 후 syntax 검사 필수

```jsx
$ sudo nginx -t
```

설정 변경 후 Nginx 재시작

```jsx
$ sudo service nginx restart
```# 🌴알고가 배포 과정

## 📘1. EC2 접속 & 도커 이미지 생성

  **1.1 파이썬 설치 (알고가 서비스 기준)**
       Python 3.6.1

 
  **1.2 도커 설치**
       Docker  20.10.5

  **1.3** **MySQL Docker 이미지 다운로드**

```jsx
$ docker pull mysql:8.0.17
```

  **1.4 Docker 이미지 확인**

```jsx
$ docker images
```

**1.5 한글이 깨지지 않도록 설정하려면 아래 인자값을 넣어주어야 한다.**

```jsx
$  --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

**1.6 Docker MySQL 컨테이너 생성 및 실행**

```jsx
$ docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ssafy1234 --name ssafy-mysql -v /Users/ssafy/datadir:/var/lib/mysql mysql:8.0.17 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

MYSQL_ROOT_PASSWORD = ssafy1234
mysql -ssafy
```

**1.7 MySQL 컨테이너 bash 쉘 접속**
docker exec 명령을 사용하여 docker 컨테이너에 접근한 다음 MySQL에 로그인한다.

```jsx
$ docker exec -it ssafy-mysql bash
$ root@f3aasdasdasd8:/#mysql -u root -p
```

mysql>

데이터베이스와 사용자를 생성하고 (컨테이너 내에서) MySQL에서 권한을 부여한다.
ssafy 사용자를 생성하고, 모든 권한을 부여한다.
변경된 권한 적용
중요 : 컨테이너 외부에서 MySQL에 로그인도 가능해야 하므로 ssafy@localhost에서 localhost 대신 %를 사용한다.
```jsx
mysql> CREATE USER 'ssafy'@'%' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'ssafy'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit
```


## 📗2. Git

2-1. git install  브랜치 master 기준

2-2. git clone  해당 서비스 주소 

---

## 📒3. EC2 접속 (1과 동일한 화면에서 진행하면 됨)

  cd s04p23a302

---

## 📕4. Frontend 배포

4-1. cd algoga-frontend

```jsx
cd algoga-frontend
```

4-2. npm install

```jsx
$ npm install
```

4-3. npm run serve    ----> 확인하는 명령어 

```jsx
$ npm run serve
```

4-4. npm run build    ——> dist 생성 

```jsx
$ npm run build
```

---

## 📕5. Backend 배포 및 가상환경 구축

 5-1. 

```jsx
$ cd algoga-backend
```

 5-2. my_settings.py 작성 [mysetting.py](http://mysetting.py/) 위치 algoga-backend/
```jsx
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'db-name',
'USER': 'xxxxx',
'PASSWORD':'xxxxx',
'HOST': 'xxxxxxx',
'PORT': '3306',
}
}

SECRET_KEY = 'xxxxxxx'

EMAIL = {
'EMAIL_BACKEND' : 'django.core.mail.backends.smtp.EmailBackend',
'EMAIL_USE_TLS' : True,
'EMAIL_PORT' : 587,
'EMAIL_HOST' : '[smtp.googlemail.com](http://smtp.googlemail.com/)',
'EMAIL_HOST_USER' : 'xxxxxx',
'EMAIL_HOST_PASSWORD' : 'xxxxxxx',
}

###########################AWS
AWS_ACCESS_KEY_ID = 'xxxxxxxX' # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = 'xxxxxxxxx' # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

###S3 Storages
AWS_STORAGE_BUCKET_NAME = 'xxxx' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%[s.amazonaws.com](http://s.amazonaws.com/)' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```
---

**xxxxx 자신의 알맞는 내용으로 넣기**


5-3. 가상환경 구축

```jsx
$ python3 -m venv env
```

5-4 . makemigrations,migrate,구동 확인

```jsx
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

algoga-backend/로 이동 

5-9. nginx설치
5-10. uwsgi 설치

5-11. sudo apt-get install nginx

```jsx
$ sudo apt-get install nginx
```

5-12. pip install uwsgi

```jsx
$ pip install uwsgi
```

5-13. vi algoga_uwsgi.ini

```jsx
$ vi algoga_uwsgi.ini
```
```jsx
[uwsgi]
chdir = /home/ubuntu/algoga1.0/s04p23a302/algoga-backend
module = backend.wsgi

socket = /home/ubuntu/algoga1.0/s04p23a302/algoga-backend/algoga.sock

socket = 127.0.0.1:8001

chmod-socket = 666
vacuum = true

#home = /home/jihun/.pyenv/versions/algoga-backend/
#virtualenv = /home/jihun/.pyenv/versions/algoga-backend/

daemonize = /home/ubuntu/algoga1.0/s04p23a302/algoga-backend/algoga_uwsgi.log

die-on-term = true
```
module : django 프로젝트를 생성하면 자동으로 생성되는 wsgi 파일을 지정한다.<br>
socket : socket 파일을 이용하는 경우 소켓이 생성될 위치와 함께 .sock 파일명을 입력한다. ip, port를 이용하고 싶은 경우 주석으로 처리된 부분과 같이 지정하면 된다.<br>
home, virtualenv : virtualenv를 이용하는 경우 가상 환경의 경로를 지정해줘야 한다.<br>
daemonize : 백그라운드로 실행 하도록 하는 설정을 하면서 로그가 저장될 파일 위치를 지정한다.<br>

가상환경 위에서 배포하시면 home,virtualenv 주석제거

5-14. $ uwsgi --ini algoga_uwsgi.ini

```jsx
 $ uwsgi --ini algoga_uwsgi.ini;
```

정상적으로 실행이 되면 memorist.sock 소켓 파일이 생성되고, 로그가 memorist_uwsgi.log에 기록된다.

5-15. algoga_uwsgi.log  // algoga.sock  생성됨

5-16. killall uwsgi; 백그라운드 에서 실행되는 백서버 죽이기

```jsx
$ killall uwsgi
```

5-17.  uwsgi --ini algoga_uwsgi.ini 백엔드서버 가동

```jsx
$ uwsgi --ini algoga_uwsgi.ini
```

5-18. sudo vim /etc/nginx/sites-enabled/default

```jsx
 sudo vim /etc/nginx/sites-enabled/default
```

nignx

5.19. frotend 경로 맞추기
5-20. backend reverse proxy 설정 추가

연결 과정
```jsx
server {
listen 80;
...
..


root /home/ubuntu/algoga1.2/s04p23a302/frontend/algoga-frontend/dist

location / {
	# First attempt to serve request as file, then
	# as directory, then fall back to displaying a 404.
	try_files $uri $uri/ =404;
}


     location /apps {

       	include uwsgi_params;
	uwsgi_pass unix:/home/ubuntu/algoga1.2/s04p23a302/backend/backend/algoga.sock;
	#backend sock 있던 위치

}
```




## 🌳6. Syntax 검사 및 Nginx 재시작 (배포과정 끝)

설정 변경 후 syntax 검사 필수

```jsx
$ sudo nginx -t
```

설정 변경 후 Nginx 재시작

```jsx
$ sudo service nginx restart
```



### ✔ 프로젝트 개발 일정

![일정](/uploads/a4767ed53b24d414f9c5208fa4912880/일정.PNG)

### ✔ 프로젝트 진행 과정

![노션관리](/uploads/61b920744a3f3df380e7eaadeb657258/노션관리.PNG)

- **진행은 <u>웹엑스, 디스코드, 노션</u>으로 협업하고 있습니다 :)** 

### ✔ 와이어프레임


    