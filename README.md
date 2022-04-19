# Customs Id Number Validator

This is a simple python package that helps validating Customs ID Number (Personal Customs Clearance Code) with name and mobile phone number.

The Customs ID Numbers (PCCC) comprises 12 digits starting with the alphabet letter P (e.g. P123123123123) and is issued by the KCS to those planning to ship personal goods into or out of Korea.

This package is suitable for overseas direct purchase e-commerce platforms that need to validate Customs Id numbers for large number of orders made on a daily basis.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install customs-id-number-validator
```

## Usage
1. 위의 명령어를 이용하여 customs-id-number-validator 패키지 설치하기
2. OPEN API Key 발급받기
    <a href="https://blog.naver.com/k_customs/222049852125">유니패스의 OPEN API Key 발급받기</a>를 참조하여 API KEY를 준비합니다.
3. unipass.ini 파일을 만들고 아래의 정보를 작성하십시오.

```bash
[DEFAULT]
UNIPASS_API_KEY=발급받은API_KEY
```

4. 파이썬 쉘에서 테스트 해보기
```python
MacBook-Pro:~/test$ pip install customs-id-number-validator

MacBook-Pro:~/test$ cat >> unipass.ini << EOF 
> [DEFAULT]
> UNIPASS_API_KEY = 발급받은API_KEY

MacBook-Pro:~/test$ ls
unipass.ini    

MacBook-Pro:~/test$ python
>>> from customs_id_number import validate
>>> validate('P123123123123', ['이름일', '이름이'], ['010-2323-2323', '010-2424-2424'])
{'success': False, 'customsIdNumber': 'P123123123123', 'name': '이름이', 'phone': '010-2424-2424', 'errors': ['납세의무자 개인통관고유부호가 존재하지 않습니다.']}
>>> validate("P2200********", ['김진', '김진*'], ['010-****-****'])
{'success': False, 'customsIdNumber': '********",', 'name': '김진*', 'phone': '010-****-****', 'errors': ['납세의무자 휴대전화번호가 일치하지 않습니다.']}
>>> validate("P2200********", ['김진', '김진*'], ['010-****-****'])
{'success': True, 'customsIdNumber': '********",', 'name': '김진*', 'phone': '010-****-****', 'errors': []}
```

5. 프로젝트에 적용하기
```python
from customs_id_number import validate;

validate('P123123123123', ['이름일', '이름이'], ['010-2323-2323', '010-2424-2424'])
```

