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

### [WBS]
![WBS](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/d3cc138d-05e3-49c5-b7b7-935a1003506f)

### [GitHub Project, Issues]
![GithubProject1](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/0c007bc6-9e9a-4d27-a433-1521a3620591)
![GithubProject2](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/d314bc11-7051-44a9-a5c3-c0b7f1911a41)

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



### [메인화면]
![메인화면](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/64e275bf-433b-46fe-b0c4-d6a537cae151)

 - 상단의 Nav bar, 배너, 하단의 설명란을 통해 Chat, Board, Login으로 이동이 가능합니다.

### [Chat]
![Chat](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/275dcf92-1347-406e-b90b-9c59ba3255a1)

 - 입력란에 사용 언어, 컨벤션을 지정한 뒤 Create 버튼을 누르면 해당 주제로 챗봇과 대화를 할 수 있는 채팅방이 생성됩니다.
 - 컨벤션은 빈 칸으로 둘 수 있으며, 그 경우 챗봇이 컨벤션 없이 해당 언어에 맞게 추천합니다.
 - 채팅방에 들어가면 '사칙연산을 위한 변수명 추천해줘' 등과 같이 물어볼 수 있습니다.

### [Board]
![Board](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/bb614782-c4d2-41ee-af80-7fdc84a7e064)

 - 공지, 질문, 잡담 카테고리의 글을 올릴 수 있는 게시판입니다.
 - 게시판 Post의 필드 중 썸네일 이미지, 제목, 내용을 List에서 출력합니다.
 - 내용의 경우 10자가 넘는다면 Slice 해 한 카드 내에서 표현할 수 있게 줄여줍니다.
 - 썸네일 이미지가 없을 경우 따로 지정한 기본이미지가 출력됩니다.

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
 
 - Django의 Template 상속과 같은 기능을 사용할 수 없어 header.js, footer.js를 통해 header, footer를 관리합니다.

### [회원가입 - 로그인]
![회원가입-로그인](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/72519b05-10c3-4f74-8165-fd65a31d811a)
 
 - 유저 모델을 커스텀하여 사용하고 있기 때문에 username 대신 email을 사용자 식별에 사용하고 있습니다.
 - 로그인을 하면 access_token, refresh_token을 발송하며 이를 local storage에 저장해 관리합니다. 로그아웃 버튼을 누르면 local storage에 저장된 토큰들을 삭제합니다.
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

### [게시판 글 쓰기]
![request_board_create](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/d85af610-06ab-4ec5-ac72-f440534ab0bc)
 
 - title, content, category, head_image를 입력하고 POST요청을 하면 게시물이 생성됩니다.
 - image의 경우 비워둘 수 있으며, created_at, updated_at은 자동설정됩니다.

### [![request_board_notice_create](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/e841b8e0-a8c2-49ca-ab6f-ee0b6944b601)]

 - 게시글 작성 중 관리자 권한이 없는 회원이 '공지' category를 설정하면 '공지글은 관리자만 작성할 수 있습니다.'라는 error 메세지를 발송합니다.

```python
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        if data.get('category') == '공지' and not self.context['request'].user.is_manager:
            raise serializers.ValidationError('공지글은 관리자만 작성할 수 있습니다.')
        return data

```

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

### 2. User모델의 운영진 권한을 가진 변수 설정 시 is_manager 사용
 
&nbsp;게시글의 '공지' 카테고리는 운영진 권한을 가진 사람만 쓰고, 수정하고, 삭제할 수 있도록 설정했습니다. 처음에는 운영진 권한을 설정할 필드로 is_staff를 사용했습니다. 다만 구현을 하기 위해 검색을 하던 도중 다음과 같은 정보를 얻었습니다.

 - is staff는 django의 기본 유저 모델에도 포함되어 있으며, is_staff가 true인 유저는 관리자 페이지에 접근이 가능하다.

 운영진이라 하더라도 관리자 페이지에 접근할 수 없도록 별도의 is_manager 필드를 적용하였습니다.

### 3. OpenAI_API의 버전과 요청 문제
 - OpenAI API의 기능 중 openai.Completion.create을 사용할 때 API의 버전에 따라 메소드명과 전송하는 메시지의 종류가 바뀌는 문제가 있었습니다.
    - `client.chat.completions.create`
      ```python
      from openai import OpenAI
      client = OpenAI()

      response = client.chat.completions.create(
         model="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
         ]
      )
      ```
    - `response = openai.ChatCompletion.create`
      ```python
      response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.gpt_messages,
                temperature=1,
            )
      ```
 - 참고하고 있던 예제와 기존 준비해두었던 프롬프트 엔지니어링 데이터를 활용하기 위해 구버전의 openAI로 다운그레이드 하였으나 24년즈음 만료될 것이라는 알림메시지를 받았습니다.


### 4. Chat_list의 POST 요청 시 400 BAD Request

#### [원인]
 - user의 id정보의 경우 로그인한 세션이 있을 경우 자동으로 생성될 것이라고 착각했기에 생긴 문제였습니다.

#### [결과]
 - BE에서 user의 id를 따로 전송해주지 않았기 때문에 FE에서 처리할 필요가 있었습니다.
 - jwt토큰을 decoding한 뒤 user의 id를 추출해 사용했습니다.
```JavaScript
// decodeJwt.mjs
export function decodeJwtToken(token) {
    if (token) {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
    }
}

// chat_list.js
import { decodeJwtToken } from './decodeJwt.mjs';
// ...
const decodedToken = decodeJwtToken($access_token);
const userId = getUserID(decodedToken);
// ...
```

### 5. Chatbot의 답변 중 개행문자 '\n'의 처리

&nbsp;프롬프트 엔지니어링을 통해 ChatGPT의 답변은 다음과 같은 형태로 정규화 되어있습니다.
```
함수명: \n 1. multiply: 곱셈을 수행하는 함수 \n 2. product: 두 개의 숫자를 곱한 결과를 반환하는 함수 \n 3. calculate_product: 곱셈 결과를 계산하는 함수 \n 4. multiply_numbers: 숫자들을 곱하는 함수 \n 5. calc_multiplication: 곱셈을 계산하는 함수 \n\n 변수: \n 1. num1, num2: 곱셈을 수행할 숫자들을 나타내는 변수 \n 2. result: 곱셈 결과를 저장하는 변수 \n 3. multiplier, multiplicand: 곱셈의 피연산자를 나타내는 변수 \n 5. operand1, operand2: 곱셈에 사용되는 피연산자를 나타내는 변수
```

이 때 평소 하듯이 p태그로 append를 하거나 innerText를 사용하면 개행문자를 인식하지 못해 저대로 출력되는 문제가 있었습니다. 처음에는 br태그로 바꿔주면 개행이 될 것이라 생각하여 다음과 같은 정규표현식을 사용했지만 여전히 개행은 되지 않고 그대로 출력되는 모습을 보였습니다.

```JavaScript
tagElement.textContent = '<chatbot>';
contentElement.innerText = item.content.replace(/\\n/g, '<br>');
```
#### [원인]
 - innerText, textContent, innerHTML의 차이
 - innerText : Element의 속성으로, 해당 Element 내에서 사용자에게 '보여지는' 텍스트 값을 읽어옵니다.
 - textContent : Node의 속성으로, display:none과 같은 style의 태그도 무시하고 해당 노드가 가지고 잇는 텍스트 값을 그대로 읽어옵니다.
 - innerHTML : Element의 속성으로, 해당 Element의 HTML을 읽고, 설정할 수 있습니다.

#### [결과]
innerText로 사용하던 부분을 innerHTML로 바꿔서 사용했습니다. 문제 없이 개행이 되는 것을 확인했습니다.

### 6. Chat_detail의 POST 요청에만 유저 요청 횟수 제한 설정
 
&nbsp;유저 별 POST 요청 횟수 제한을 위해 Throttle 기능을 적용하였습니다. 다만 ChatDetailView는 한 클래스 내에서 GET과 POST 메소드를 정의하고 있기 때문에 class에 throttle을 적용할 경우 GET메소드에도 요청 제한이 걸리는 문제가 있었습니다.
```python
class ChatDetailView(APIView):
    permission_classes = [IsOwnerAndAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, chat_pk):
      #   ...
    def post(self, request, chat_pk):
      #   ...
```
검색을 하다보니 throttle을 데코레이터로 사용이 가능하며, 이를 메소드에 걸 수 있다는 내용을 발견했습니다.
```python
class ChatDetailView(APIView):
   permission_classes = [IsOwnerAndAuthenticated]

   def get(self, request, chat_pk):
      #   ...
   @throttle_classes([UserRateThrottle])
   def post(self, request, chat_pk):
      #   ...
```
데코레이터로 throttle을 설정했을 때는 GET요청에도, POST요청에도 제한이 걸리지 않았습니다.
이후 검색하다 나온 다른 결과로는, throttle_scope를 통해 특정 메소드에만 설정할 수 있다는 내용이 있었습니다.
```python
class ChatDetailView(APIView):
   permission_classes = [IsOwnerAndAuthenticated]
   throttle_classes = [UserRateThrottle]
   throttle_scope = "post"

   def get(self, request, chat_pk):
      #   ...
   def post(self, request, chat_pk):
      #   ...
```
scope를 설정해보았지만 처음과 같이 GET요청에도 횟수 제한이 걸려버렸습니다.

#### [결과]

&nbsp;몇 번의 시행착오 결과, POST메소드에만 throttle을 걸기 위해서는 View를 새로 만드는 것이 낫다는 결론을 얻었습니다.
```python
class UserCreateAPIView(CreateAPIView):
    '''
    User Create
    '''


class UserViewSet(ModelViewSet):
   '''
    User RUD
    '''
```
이런 형태와 같이 Create와 Read, Update, Delete를 담당하는 View를 별개의 class로 만들었다면 throttle을 따로 걸 수 있었을 것으로 생각됩니다.

<div align="right">

[목차로](#목차)

</div>

## <개발 회고>

 - GitHub의 Project와 Isuue 트래킹을 통한 관리
   - WBS 기획을 하듯이 프로젝트의 구체적 목표를 Issue로 만들어 개발 목표를 정하고 우선순위를 따지는 것이 용이했습니다.

 - TDD의 유용성 체감 
   - 코드의 구현도 하기 전에 model의 내용만 가지고 테스트를 하는 것이 무슨 의미가 있을까? 싶었지만 한번 사용해보면서 체감을 할 수 있었습니다.
   - 어느 URL에 POST요청을 보낼 때 어떠한 값이 들어있어야 하고, 어떤 값이 반환되는지 미리 테스트하면서 확인해두는 것이 BE 개발을 하면서도, FE에서 fetch 구현을 하면서도 큰 도움이 될 수 있었습니다.

  ### 개선할 점
 - 시간 분배에 익숙해질 것, 오류가 발생했을 때 여유를 가질 것
   - 제한된 시간 내에 BE, FE를 모두 구현해야 하는 프로젝트
   - 낯선 프레임워크, API다보니 따로 공부할 시간도 더 필요했습니다.
   - 시간이 모자란 상황에서 프로젝트를 하다보니 따로 트러블슈팅을 위한 문서화가 부족했으며, 부랴부랴 해결하고 넘어가 기억에 남지 않는 오류도 있었습니다.
   - 서두르나 차분히하나 시간 차이는 크게 나지 않으니 필요한 부분은 기록하여 더 확실히 배우고 넘어갈 필요가 있다고 생각됩니다.

 - 자신이 사용하고 있는 프레임워크, API의 버전을 알고 사용할 것
   - Python과 같은 언어는 크게 바뀌는 일이 잘 없다보니 오래된 정보라도 문제 없는 경우가 많았습니다.
   - Django, OpenAI API의 경우 구버전에서의 자료가 너무 많이 나와 다루는데 애로사항이 생겼고, 검색을 해봐도 서로 내용이 달라 어느 것을 따라야 할 지 난감한 상황이 많았습니다.
   - 특히 검색해서 나오는 각종 예제보다 공식문서를 더 활용하는 것이 더 수월하다는 경험을 얻었습니다.

<div align="right">

[목차로](#목차)

</div>
