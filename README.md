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
 - 메인 UI 이후 마인드맵, WBS, 와이어프레임, 폴더구조, 플로우차트, ERD 등
 - 메인 기능 간략 설명

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
<img src="https://img.shields.io/badge/amazonaws-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>

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

### [Flowchart]
![플로우차트_1](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/490744aa-da5d-4420-a8c2-436be81d3142)

### [Wireframe]
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
|URL|페이지 설명|GET|POST|PUT|DELETE|
|------|---|:---:|:---:|:---:|:---:|
|/accounts/login|로그인|- [ ]|- [x]|- [ ]|- [ ]|
|/accounts/logout|로그아웃|- [ ]|- [x]|- [ ]|- [ ]|
|/accounts/signup|회원가입|- [ ]|- [x]|- [ ]|- [ ]|
|/accounts/profile|프로필 <br> 프로필 수정 <br> 회원 탈퇴|- [x]|- [ ]|- [x]|- [x]|
|/accounts/token/refresh|토큰갱신|- [ ]|- [x]|- [ ]|- [ ]|
|/board|게시글 목록 <br> 게시글 생성|- [x]|- [x]|- [ ]|- [ ]|
|/board/{postid}|게시글 상세 <br> 게시글 수정 <br> 게시글 삭제|- [x]|- [ ]|- [x]|- [x]|
|/chat|채팅 목록 <br> 채팅 생성 <br> 채팅 삭제|- [x]|- [x]|- [ ]|- [x]|
|/chat/{chatid}|채팅 상세 <br> 메시지 발송|- [x]|- [x]|- [ ]|- [ ]|


<div align="right">

[목차로](#목차)

</div>

## <기능 설명>


<div align="right">

[목차로](#목차)

</div>

## <개발 이슈>


<div align="right">

[목차로](#목차)

</div>

## <개발 회고>


<div align="right">

[목차로](#목차)

</div>
