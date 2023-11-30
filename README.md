# 변수/함수명 추천 챗봇

&nbsp;이스트소프트에서 주관하는 백엔드 개발자 부트캠프 '오르미'에서 만든 프로젝트입니다. HTML, 자바스크립트를 만들 때 사용했던 아이디어 'GPT에게 변수명/함수명 추천받기'를 사용하여 제작하였습니다.

&nbsp;OpenAI의 API를 사용해 로그인한 사용자들에게 챗GPT의 답변을 제공하는 사이트입니다. Django의 DRF를 사용해 BE와 FE를 별개로 만드는 식으로 개발되었습니다.

&nbsp;개발 기간은 11.21~11.30 총 10일이었으며 1인개발로 진행되었습니다.

GitHub Repository : https://github.com/jmkim648/Ormi-Chatbot-BE

FE Repository : https://github.com/jmkim648/Ormi-Chatbot-FE

## <목차>
[1. 요구사항 명세](#요구사항-명세)

[2. 개발 기술 및 환경](#개발-기술-및-환경)

[3. 주요 기능](#주요-기능)

[4. API 명세](#api-명세)

[5. 기능 설명](#기능-설명)

[6. 개발 이슈](#개발-이슈)

[7. 개발 회고](#개발-회고)

## <요구사항 명세>
### [기본 요구사항]
- DRF를 이용하여 구현할 것
- CBV를 사용할 것
- 회원가입, 로그인 구현
- FE -> BE(Django server) -> OpenAI API api -> FE 의 구조를 거쳐 반영
- 챗봇 API는 로그인 한 사용자만 사용 가능
- 각 유저 당 하루 5번만 요청할 수 있도록 제한
- 채팅(챗봇 상담)내역을 저장, 조회할 수 있도록 구현
- 각 저장 내역은 로그인한 본인만 볼 수 있도록 구현


### [선택 요구사항]
- 라이트세일을 이용하여 FE, BE 서버 배포
- 개인 도메인 등록, FE, BE 배포 : https 추가, front는 따로 배포(github pages 등)
- kakao, github 등 OAuth2 연결해보기

<div align="right">

[목차로](#목차)

</div>

## <개발 기술 및 환경>

### [Environment]
<img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/visualstudio-007ACC?style=flat-square&logo=visualstudio&logoColor=white"/>

### [Frontend]
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=white">
<img src="https://img.shields.io/badge/tailwindcss-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>

### [Backend]
<img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>

### [DB]
<img src="https://img.shields.io/badge/sqlite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>


<div align="right">

[목차로](#목차)

</div>

## <주요 기능>

### [메인화면]
![메인화면](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/64e275bf-433b-46fe-b0c4-d6a537cae151)

### [WBS]
![WBS](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/d3cc138d-05e3-49c5-b7b7-935a1003506f)

### [Mindmap]
![MINDMAP_1](https://github.com/STP-TP/CMI.DB-Collector/assets/22714585/d6b0f005-cd91-4356-bfb9-f8d5b57bcc0f)

### [ERD]
![ERD_3](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/2eb0b074-848a-4413-8d41-919210819711)

### [Folder Tree]

```
📦 Ormi-Chatbot-BE
├─ .gitignore
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ board
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ permissions.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ chat
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ permissions.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ chatbot
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ utils
│  │  └─ openAI_API.py
│  └─ wsgi.py
├─ manage.py
└─ requirements.txt
```
```
📦 Ormi-Chatbot-FE
├─ .vscode
│  └─ settings.json
├─ README.md
├─ board_detail.html
├─ board_list.html
├─ chat_detail.html
├─ chat_list.html
├─ index.html
├─ login.html
├─ signup.html
└─ js
   ├─ chat_detail.js
   ├─ chat_list.js
   ├─ decodeJwt.mjs
   ├─ footer.js
   ├─ header.js
   ├─ login.js
   ├─ signup.js
   └─ token_refresh.mjs
```


### [Flowchart]
![플로우차트_1](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/490744aa-da5d-4420-a8c2-436be81d3142)

### [Mockup Page]
|||
|------|---|
|![01_Main](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/16f32e2c-3882-49b2-b666-296c61230a1f)메인화면|![02_Login](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/1075c75b-bed8-40fe-a73f-3ddcd0f2ffda)로그인|
|![03_Signup](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/73a7819c-fee5-444b-a2f9-a510b0497fd1)회원가입|![04_Profile](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/79f65ed5-f5ef-4530-af86-8358286a1f2c)프로필|
|![05_Board](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/b60ec794-cc85-4020-833b-63e52c4a7d89)게시판리스트|![06_Board detail](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/718f49bf-5788-4f2f-ae46-834d60102c84)게시판 디테일|
|![07_Chat](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/9a6df776-78af-4beb-a6cd-f4dbc18d2c7f)채팅리스트|![08_Chat detail](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/deb6c742-3f28-499c-bd52-bfe9ed792b46)채팅 디테일|

<div align="right">

[목차로](#목차)

</div>

## <API 명세>
|URL|페이지 설명|GET|POST|PUT|DELETE|로그인 권한| 작성자 권한|
|------|---|:---:|:---:|:---:|:---:|:---:|:---:|
|/accounts/login|로그인| |✔️| | | | |
|/accounts/logout|로그아웃| |✔️| | | | |
|/accounts/signup|회원가입| |✔️| | | | |
|/accounts/profile|프로필 <br> 프로필 수정 <br> 회원 탈퇴|✔️| |✔️|✔️|✔️ <br> ✔️ <br> ✔️|<br> ✔️ <br> ✔️
|/accounts/token/refresh|토큰갱신| |✔️| | | | |
|/board|게시글 목록 <br> 게시글 생성|✔️|✔️| | | <br> ✔️| |
|/board/{postid}|게시글 상세 <br> 게시글 수정 <br> 게시글 삭제|✔️| |✔️|✔️| <br> ✔️ <br> ✔️ | <br> ✔️ <br> ✔️
|/chat|채팅 목록 <br> 채팅 생성|✔️|✔️| |✔️| ✔️<br>✔️| 
|/chat/{chatid}|채팅 상세 <br> 메시지 발송 <br> 채팅 삭제|✔️|✔️| | | ✔️ <br> ✔️ <br> ✔️ | ✔️ <br> ✔️ <br> ✔️

- 게시판 글 작성 중 카테고리가 '공지'인 경우, 매니저 권한이 있는 회원만 글을 작성할 수 있습니다.


<div align="right">

[목차로](#목차)

</div>

## <기능 설명>

### [메인화면]
![메인화면](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/2ef0dca5-1b45-4568-a4fa-2c75c112bf9b)
 - 헤더의 로고, Nav 글자들은 해당 페이지로 링크됩니다.
 - 배너의 버튼과 게시판의 버튼은 각각 Chat과 Board 페이지로 연결됩니다.

### [회원가입 - 로그인]
![회원가입-로그인](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/72519b05-10c3-4f74-8165-fd65a31d811a)
 - 유저 모델을 커스텀하여 사용하고 있기 때문에 username 대신 email을 사용자 식별에 사용하고 있습니다.
 - 회원가입을 할 때는 email, password, password 확인, nickname을 입력해야하며, 로그인을 할 때는 email, password를 요구합니다.
 - access token이 만료될 경우 refresh token을 통해 갱신해야합니다. board와 chat 페이지에서 POST요청을 보낼 때 토큰이 만료되었는지 확인하는 절차를 거치도록 구현하였습니다.

### [채팅방 목록 - 채팅방 생성]
![채팅방 목록-생성](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/bc5112e7-99fa-475f-8049-c6d88ed86095)
 - 로그인 한 유저만 채팅방 목록에 접속 가능하며, 채팅방 목록 페이지에서만 채팅방 생성 접근이 가능합니다.
 - 로그인한 유저의 ID로 생성된 채팅방의 목록을 받아와 출력합니다.
 - 상단의 Language, Convention란을 입력 후 버튼을 누르면 채팅방이 생성됩니다.
 - Convention은 비워놓은 채로 생성할 수 있습니다.
 - 채팅방을 생성할 때 설정된 Language, Convention을 통해 ChatGPT의 프롬프트 엔지니어링을 진행합니다.

### [채팅 내용 읽기]
![챗 내용 읽기](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/40c328da-91be-44da-9cb3-16f488cd2284)
 - 해당 채팅방의 채팅 내용을 받아와 출력합니다.
 - DB에 있는 메시지를 생성날짜 순서대로 정렬해 받아오며, is_user가 true일 경우 사용자의 메시지, false일 경우 챗봇의 메시지로 분류합니다.
 - 사용자의 메시지는 우측으로, 챗봇의 메시지는 좌측으로 정렬하여 출력합니다.
 - 프롬프트 엔지니어링을 통해 챗봇의 답변에 개행문자 '\n'이 포함되어 있기 때문에 별도의 작업을 거쳐 개행문자를 인식하도록 하였습니다.

### [채팅 내용 전송]
![챗 내용 전송](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/43088ec7-ec8e-4775-9eb9-e98353bc26d3)
 - 사용자가 질문을 입력 후 send 버튼을 누르면 해당 메시지와 프롬프트 엔지니어링을 위한 데이터를 전송합니다.
 - 메시지를 전송할 때, 답변을 받았을 때 바로 메시지를 DB에 저장하며 출력화면에도 메시지가 반영됩니다.

### [게시판 목록]
![게시판목록](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/7fbb91a3-c76e-43be-a9c4-3405d1304372)
 - GET 메소드의 경우 로그인을 하지 않아도 접근이 가능하며, 모든 사용자의 게시글이 출력됩니다.
 - 게시판 목록에서는 해당 게시글의 썸네일 이미지, 제목, 내용을 출력합니다. 내용의 길이가 10자를 넘을 경우 card의 크기에 맞도록 잘라내어 출력합니다.

### [로그인 권한 필요]
![로그인 요구](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/7ecaefc2-9e22-4641-9e5f-8175c002db21)
 - 로그인을 하지 않은 채로 로그인 권한이 필요한 곳에 접속할 경우 alert를 통해 '로그인 후 사용해주세요' 메시지를 띄워주며 login페이지로 전송합니다.

<div align="right">

[목차로](#목차)

</div>

## <개발 이슈>

### 1. admin페이지에서 login 불가
&nbsp;BE 프로젝트를 만들고 Init을 마친 뒤 처음으로 구현에 착수한 것은 User모델 커스텀이었습니다. 재량껏 커스텀 뒤 superuser를 만들고 admin페이지에서 로그인을 하는데 에러가 발생했습니다.
```
DoesNotExist at /admin/login Site matching query does not exist.
```
처음에는 유저 모델을 커스텀하던 중 유저 매니저나 admin페이지에의 반영에 문제가 생긴 것으로 판단하여 프로젝트를 새로 만들었습니다. 하지만 기본 유저 모델을 사용해도 또 같은 에러가 발생했습니다.

#### [원인]
 - Django가 DB에 가지고 있던 사이트 정보가 사라진 것
 - 개발 도중 프로젝트를 새로 만들겠다고 DB를 날려버리고 새로 생성하는 과정에서 오류가 발생한 것으로 추정
#### [해결]
```shell
python manage.py shell

>>>from django.contrib.sites.models import Site
>>>Site.objects.create(name='your_site_name', domain='your_site_domain')
```
해당 작업을 한 뒤 settings.py에서
```
SITE_ID = 1
```
설정을 해주고 나서야 login을 할 수 있었습니다.

### 2. User모델의 운영진 권한을 가진 변수 설정 시 is_staff 사용
 - is staff는 django의 기본 유저 모델에도 포함되어 있으며, is_staff가 true인 유저는 관리자 페이지에 접근이 가능한 문제
 - 운영진이라 하더라도 관리자 페이지에 접근할 수 없도록 별도의 is_manager 필드를 생성

### 3. OpenAI_API의 버전과 요청 문제
 - OpenAI API의 기능 중 chat.Completion을 사용할 때 API의 버전에 따라 메소드명과 전송하는 메시지의 종류가 바뀌는 문제
 - 기존 준비해두었던 프롬프트 엔지니어링 데이터를 활용하기 위해 구버전의 openAI를 설치하였으나 24년즈음 만료될 것이라는 알림메시지


### 4. FE(VSC liveserver) -> BE(django의 python manage.py runserver) 연결 문제
 - corsheaders 설치

### 5. Chat_list의 POST 요청 시 400 BAD Request
 - user의 id정보의 경우 로그인한 세션이 있을 경우 자동으로 생성될 것이라고 착각했기에 생긴 문제
 - jwt토큰을 decoding한 뒤 user의 id를 추출해내는 작업이 필요

### 6. Chatbot의 답변 중 개행문자 '\n'의 처리
 - innerText, innerHTML, textcontent의 차이

### 7. Chat_detail의 POST 요청에만 유저 요청 횟수 제한 설정
 - ```
   throttle_classes = [UserRateThrottle]
   throttle_scope = "post"
    ```
   코드를 통해 쓰로틀을 적용하려 했으나 GET 요청에도 제한이 걸리는 문제 발생


<div align="right">

[목차로](#목차)

</div>

## <개발 회고>
 - 자신이 사용하고 있는 프레임워크, API의 버전을 알고 사용할 것
   - Python과 같은 언어는 크게 바뀌는 일이 잘 없다보니 오래된 정보라도 문제 없는 경우가 많은데
   - Django, OpenAI API의 경우 구버전에서의 자료가 너무 많이 나와 다루는데 애로사항

 - 오류가 발생했을 때 여유를 가질 것 
   - 시간이 모자란 상황에서 프로젝트를 하다보니 따로 트러블슈팅을 위한 문서화 부족
   - 서두르나 차분히하나 시간 차이는 크게 나지 않으니 필요한 부분은 기록하여 더 배울 수 있도록

 - 시간 분배에 익숙해질 것
   - 제한된 시간 내에 BE, FE를 모두 구현해야 하는 프로젝트
   - 낯선 프레임워크, API다보니 공부할 시간도 필요

 - GitHub의 Project와 Isuue 트래킹을 통한 관리
   - WBS 기획을 하듯이 프로젝트의 구체적 목표를 Issue로 만들어 개발 목표를 정하고 우선순위를 따지는 것이 용이

<div align="right">

[목차로](#목차)

</div>
