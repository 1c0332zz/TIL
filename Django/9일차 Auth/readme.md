## Django Auth 

### Django Auth 개요

* Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)하고 있음
  * User
  * 권한 및 그룹 
  * 암호 해시 시스템 
  * Form 및 View 도구 
  * 기타 적용가능한 시스템
* 필수 구성은 settings.py의 INSTALLED_APPS에서 확인 가능
  * django.contrib.auth
* Authentication (인증) 
  * 신원 확인 
  * 사용자가 자신이 누구인지 확인하는 것
* Authorization (권한, 허가) 
  * 권한 부여 
  * 인증된 사용자가 수행할 수 있는 작업을 결정

## User model 활용하기

### Django User Model

* “Custom User Model로 대체하기” 
* Django는 기본적인 인증 시스템과 여러 가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체함
* Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분 하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장(highly recommended) 
* 커스텀 User 모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문 
  * 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함
* 개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절하지 않을 수 있음 
  * 예를 들어, 내 서비스에서 회원가입 시 username 대신 email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우, Django의 User Model은 기본적으로 username를 식별 값으로 사용하기 때문에 적합하지 않음 
* Django는 현재 프로젝트에서 사용할 User Model을 결정하는 AUTH_USER_MODEL 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함