<div align="center">

# 디프만 슬랙 관리용 봇

[![Build Status](https://travis-ci.org/depromeet/slackbot-management.svg?branch=master)](https://travis-ci.org/depromeet/slackbot-management) [![CircleCI](https://circleci.com/gh/depromeet/slackbot-management.svg?style=svg)](https://circleci.com/gh/depromeet/slackbot-management) [![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

</div>


## 봇 개발하기

레포 `clone` 후 패키지를 설치해줍시다.

```
$ git https://github.com/depromeet/slackbot-management
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

그 다음 `handler.py` 에 람다 함수를 작성하시면 됩니다!

**이 슬랙봇 api 는 AWS Lambda 에 배포되었으며, `serverless` 프레임워크를 사용하여 개발되었습니다.**  
**파이썬 3.6.4 런타임 환경입니다**

## License
MIT
