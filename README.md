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

### [Mindmap]
![MINDMAP_1](https://github.com/STP-TP/CMI.DB-Collector/assets/22714585/d6b0f005-cd91-4356-bfb9-f8d5b57bcc0f)

### [ERD]
![ERD_1](https://github.com/STP-TP/CMI.DB-Collector/assets/22714585/7660e36a-06c0-4d20-b8e6-51f7fd83592c)

### [Folder Tree]

### [Flowchart]

### [Wireframe]


<div align="right">

[목차로](#목차)

</div>

## <API 명세>


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
