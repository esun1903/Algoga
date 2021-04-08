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
jmlim이라는 사용자를 생성하고, 모든 권한을 부여한다.
변경된 권한 적용
중요 : 컨테이너 외부에서 MySQL에 로그인도 가능해야 하므로 jmlim@localhost에서 localhost 대신 %를 사용한다.

mysql> CREATE USER 'jmlim'@'%' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'jmlim'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit

---

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

---

### 가상환경 구축

**xxxxx 자신의 알맞는 내용으로 넣기**
5-3. python3 -m venv env

```jsx
$ python3 -m venv env
```

5-5. python [manage.py](http://manage.py/) makemigrations

```jsx
$ python [manage.py](http://manage.py/) makemigrations
```

5-6. python [manage.py](http://manage.py/) migrate

```jsx
$ python [manage.py](http://manage.py/) migrate
```

5-7. python [manage.py](http://manage.py/) runserver 서버 구동 확인

```jsx
$ python [manage.py](http://manage.py/) runserver
```

5-8. algoga-backend/

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

module : django 프로젝트를 생성하면 자동으로 생성되는 wsgi 파일을 지정한다.
socket : socket 파일을 이용하는 경우 소켓이 생성될 위치와 함께 .sock 파일명을 입력한다. ip, port를 이용하고 싶은 경우 주석으로 처리된 부분과 같이 지정하면 된다.
home, virtualenv : virtualenv를 이용하는 경우 가상 환경의 경로를 지정해줘야 한다.
daemonize : 백그라운드로 실행 하도록 하는 설정을 하면서 로그가 저장될 파일 위치를 지정한다.

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

--------------------------------연결 과정
nignx

server {
listen 80;
...
..

5.19. frotend 경로 맞추기
root /home/ubuntu/algoga1.2/s04p23a302/frontend/algoga-frontend/dist

location / {
	# First attempt to serve request as file, then
	# as directory, then fall back to displaying a 404.
	try_files $uri $uri/ =404;
}

5-20. backend reverse proxy 설정 추가

     location /apps {

       	include uwsgi_params;
	uwsgi_pass unix:/home/ubuntu/algoga1.2/s04p23a302/backend/backend/algoga.sock;
	#backend sock 있던 위치

}

---

## 🌳6. Syntax 검사 및 Nginx 재시작 (배포과정 끝)

설정 변경 후 syntax 검사 필수

```jsx
$ sudo nginx -t
```

설정 변경 후 Nginx 재시작

```jsx
$ sudo service nginx restart
```