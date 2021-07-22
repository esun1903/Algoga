## 알고가📕 - 알고리즘을 알고가

![https://user-images.githubusercontent.com/68232654/119593578-33591980-be15-11eb-9e58-2db1c1bb0602.png](https://user-images.githubusercontent.com/68232654/119593578-33591980-be15-11eb-9e58-2db1c1bb0602.png)

## ✏️프로젝트 개요

<b>프로젝트 기간 : 2021.03.08 ~ 2021.04.09</b>

**알고가 - 알고리즘 문제 풀이 능력을 높여주는 알고리즘 문제 추천 서비스**

- 알고리즘 공부를 막 시작하거나, 많이 풀었지만 실력이 잘 향상되지 않는 경우를 위한 알고리즘 문제 추천 및 정리 플랫폼입니다.
- 내가 푼 문제를 기반으로 내가 자주 틀리는 유형, 많이 풀었지만 보충할 유형 등 내가 풀면 좋은 문제들을 추천해줍니다.
- 문제를 풀고 내가 푼 문제를 정리하고 다른 사람들과 문제 풀이 방법을 공유하며 실력을 향상시킬 수 있습니다.

<br>

## 👩🏻‍💻👨🏻‍💻알고가를 만든 사람들

| 팀원   | 역할    |
| ------ | ------- |
| 최은선 | BE      |
| 표기동 | BE      |
| 권영일 | BE      |
| 이동희 | FE    |
| 박철완 | FE    |


<br>

### ❓ 문제인식
<br>
<img src = "[https://user-images.githubusercontent.com/68232654/119594053-0ce7ae00-be16-11eb-8639-40ed9a5383a2.png](https://user-images.githubusercontent.com/68232654/119594053-0ce7ae00-be16-11eb-8639-40ed9a5383a2.png)" width="800px">

### 👨🏻‍💼 페르소나 설정

알고리즘을 잘 하고 싶은 취업준비생 비전공생 김알못, 전공생 김알고
<br>
<img src = "[https://user-images.githubusercontent.com/38427646/126605603-d1897cec-f187-4526-917c-d2c928341ff0.png](https://user-images.githubusercontent.com/38427646/126605603-d1897cec-f187-4526-917c-d2c928341ff0.png)" width="800px">
### 💁🏻‍♀️ 해결방안

<br>

<img src = "[https://user-images.githubusercontent.com/38427646/126605707-b39a7acf-cc36-4d62-8bd6-eb403883f9dd.png](https://user-images.githubusercontent.com/38427646/126605707-b39a7acf-cc36-4d62-8bd6-eb403883f9dd.png" width="800px">


### ✔️ 주요 서비스 기능

1. 메인페이지 - 회원가입시 입력 받은 **백준 아이디를 기반으로 문제 추천**

2. 메인페이지 - 프로필 및 **깃허브 잔디심기**🌱 기능 (일자별로 검색 가능)

3. 마이페이지 - 자신이 푼 문제와 로그, 문제 추천 목록 확인

4. 문제 등록 - 사용자가 푼 문제들을 **유형별&언어별에 맞추어 작성** 및 그에 대한 **설명은** **마크다운**으로 작성 가능

5. 풀이 확인 - 문제 별로 자신의 풀이 방법과 **공개되어 있는 다른 사람들의 풀이 공유 가능** 

6. 다크모드 / 기본모드 기능 

### 🌱 Tech Log & Cooperation

진행 상황은 **스크럼과 회의록**을 통해 진행하고 있습니다.

**1일 1스크럼**으로 노션에 올려 이슈들을 공유하고 있으며

**회의를 진행 시 회의록을 작성**하여 일차별로 정리하고 있습니다.

<br>

### [실제 홈페이지](http://i4a303.p.ssafy.io/)
### [컨벤션](https://www.notion.so/332cddb89bff4354b3aee8bc1d2746a8)
### 🌱 Tech Stack
### System architecture

<img src = "[https://user-images.githubusercontent.com/38427646/126262711-ae506989-798f-4143-978a-882827bdd6ef.png](https://user-images.githubusercontent.com/68232654/119595810-158db380-be19-11eb-81d8-b70d8ed77e9d.png)" width="800px">

<br>

<details>
<summary><b>✔️ERD</b></summary>
<img src = "[https://user-images.githubusercontent.com/38427646/126273089-c15b39f8-c1eb-4cff-a8c9-f6d9caf6aee0.png](https://user-images.githubusercontent.com/68232654/119595178-1a059c80-be18-11eb-8202-5f4d6675040f.png)" width="800px">
</details>

<details>
<summary><b>✔️APITable</b></summary>
<img src = "[https://user-images.githubusercontent.com/38427646/126273089-c15b39f8-c1eb-4cff-a8c9-f6d9caf6aee0.png](https://user-images.githubusercontent.com/68232654/119595178-1a059c80-be18-11eb-8202-5f4d6675040f.png)" width="800px">

<img src = "[https://user-images.githubusercontent.com/38427646/126273089-c15b39f8-c1eb-4cff-a8c9-f6d9caf6aee0.png"](https://user-images.githubusercontent.com/68232654/119596269-ce53f280-be19-11eb-9e13-77f4abfa5768.png) width="800px">
</details>
<details>
<summary><b>💻 실행 방법</b></summary>

#### 알가 배포 과정

##### 📘1. EC2 접속 & 도커 이미지 생성

**1.1 파이썬 설치 (알고가 서비스 기준)**
Python 3.6.1

**1.2 도커 설치**
Docker  20.10.5

**1.3** **MySQL Docker 이미지 다운로드**

```
$ docker pull mysql:8.0.17

```

**1.4 Docker 이미지 확인**

```
$ docker images

```

**1.5 한글이 깨지지 않도록 설정하려면 아래 인자값을 넣어주어야 한다.**

```
$  --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

```

**1.6 Docker MySQL 컨테이너 생성 및 실행**

```
$ docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ssafy1234 --name ssafy-mysql -v /Users/ssafy/datadir:/var/lib/mysql mysql:8.0.17 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

MYSQL_ROOT_PASSWORD = ssafy1234
mysql -ssafy

```

**1.7 MySQL 컨테이너 bash 쉘 접속**
docker exec 명령을 사용하여 docker 컨테이너에 접근한 다음 MySQL에 로그인한다.

```
$ docker exec -it ssafy-mysql bash
$ root@f3aasdasdasd8:/#mysql -u root -p

```

mysql>

데이터베이스와 사용자를 생성하고 (컨테이너 내에서) MySQL에서 권한을 부여한다.
ssafy 사용자를 생성하고, 모든 권한을 부여한다.
변경된 권한 적용
중요 : 컨테이너 외부에서 MySQL에 로그인도 가능해야 하므로 ssafy@localhost에서 localhost 대신 %를 사용한다.

```
mysql> CREATE USER 'ssafy'@'%' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'ssafy'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit

```

##### 📗2. Git

2-1. git install  브랜치 master 기준

2-2. git clone  해당 서비스 주소

---

##### 📒3. EC2 접속 (1과 동일한 화면에서 진행하면 됨)

cd s04p23a302

---

##### 📕4. Frontend 배포

4-1. cd algoga-frontend

```
cd algoga-frontend

```

4-2. npm install

```
$ npm install

```

4-3. npm run serve    ----> 확인하는 명령어

```
$ npm run serve

```

4-4. npm run build    ——> dist 생성

```
$ npm run build

```

---

##### 📕5. Backend 배포 및 가상환경 구축

5-1.

```
$ cd algoga-backend

```

5-2. my_settings.py 작성 [mysetting.py](http://mysetting.py/) 위치 algoga-backend/

```
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
'EMAIL_HOST' : '[smtp.googlemail.com](<http://smtp.googlemail.com/>)',
'EMAIL_HOST_USER' : 'xxxxxx',
'EMAIL_HOST_PASSWORD' : 'xxxxxxx',
}

###########################AWS
AWS_ACCESS_KEY_ID = 'xxxxxxxX' # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = 'xxxxxxxxx' # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

###S3 Storages
AWS_STORAGE_BUCKET_NAME = 'xxxx' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%[s.amazonaws.com](<http://s.amazonaws.com/>)' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

```

---

**xxxxx 자신의 알맞는 내용으로 넣기**

5-3. 가상환경 구축

```
$ python3 -m venv env

```

5-4 . makemigrations,migrate,구동 확인

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```

algoga-backend/로 이동

5-9. nginx설치
5-10. uwsgi 설치

5-11. sudo apt-get install nginx

```
$ sudo apt-get install nginx

```

5-12. pip install uwsgi

```
$ pip install uwsgi

```

5-13. vi algoga_uwsgi.ini

```
$ vi algoga_uwsgi.ini

```

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

```

module : django 프로젝트를 생성하면 자동으로 생성되는 wsgi 파일을 지정한다.<br>
socket : socket 파일을 이용하는 경우 소켓이 생성될 위치와 함께 .sock 파일명을 입력한다. ip, port를 이용하고 싶은 경우 주석으로 처리된 부분과 같이 지정하면 된다.<br>
home, virtualenv : virtualenv를 이용하는 경우 가상 환경의 경로를 지정해줘야 한다.<br>
daemonize : 백그라운드로 실행 하도록 하는 설정을 하면서 로그가 저장될 파일 위치를 지정한다.<br>

가상환경 위에서 배포하시면 home,virtualenv 주석제거

5-14. $ uwsgi --ini algoga_uwsgi.ini

```
 $ uwsgi --ini algoga_uwsgi.ini;

```

정상적으로 실행이 되면 memorist.sock 소켓 파일이 생성되고, 로그가 memorist_uwsgi.log에 기록된다.

5-15. algoga_uwsgi.log  // algoga.sock  생성됨

5-16. killall uwsgi; 백그라운드 에서 실행되는 백서버 죽이기

```
$ killall uwsgi

```

5-17.  uwsgi --ini algoga_uwsgi.ini 백엔드서버 가동

```
$ uwsgi --ini algoga_uwsgi.ini

```

5-18. sudo vim /etc/nginx/sites-enabled/default

```
 sudo vim /etc/nginx/sites-enabled/default

```

nignx

5.19. frotend 경로 맞추기
5-20. backend reverse proxy 설정 추가

연결 과정

```
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

##### 6. Syntax 검사 및 Nginx 재시작

설정 변경 후 syntax 검사 필수

```
$ sudo nginx -t

```

설정 변경 후 Nginx 재시작

```
$ sudo service nginx restart

```

</details>
