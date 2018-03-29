# 디프만 슬랙 관리용 봇

[![Build Status](https://travis-ci.org/depromeet/slackbot-management.svg?branch=master)](https://travis-ci.org/depromeet/slackbot-management) [![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)


## 봇 개발하기

레포 `clone` 후 패키지를 설치해줍시다.

```
$ git https://github.com/depromeet/slackbot-management
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

**이 슬랙봇 api 는 AWS Lambda 에 배포되었으며, `serverless` 프레임워크를 사용하여 개발되었습니다.**  
**파이썬 3.6.4 런타임 환경입니다**

## 배포 패키지 만들기

### 외부 라이브러리
배포 패키지를 만들 때는 `requirements` 들을 프로젝트 루트 폴더에 설치해야 합니다. 그렇게 하기 위해서 다음 명령어를 입력해줍시다.
```
$ pip install -r requirements.txt -t .
```

그 다음에, 설치된 패키지들의 폴더명을 전부 `.gitignore` 에 추가해줍시다.

### 함수 명시하기
구현하신 람다 함수를 `serverless.yml` 에 명시해주셔야 합니다. 다음과 같은 형식을 따르시면 됩니다.

```YAML
<function_name>:
    handler: <path/to/handler>
    description: description
    events:
      - event 1
      - event 2
```

해당 형식으로 `serverless.yml` 의 `functions` 밑에 적어주시면 됩니다.
자세한 내용은 [공식 문서](https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/) 를 참조해 주세요.

### 배포하기

다음 명령어를 사용하여 패키지 전체 배포가 가능합니다.
```
$ sls deploy
```

만약 특정한 함수만 수정하셨다면, 해당 함수만 배포가 가능합니다. `<function_name>` 은 `serverless.yml` 에 적으신 `function_name` 과 동일해야 합니다.
```
$ sls deploy function -f <function_name>
```

## 슬랙봇 명령어 목록

[wiki](https://github.com/depromeet/slackbot-management/wiki) 에서 열람하실 수 있습니다. 또한, 슬랙 채널에 `@디프만 명령어` 를 입력하셔도 보여집니다.

## License
MIT
