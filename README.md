# Customs Id Number Validator

This is a simple python package that helps validating Customs ID Number (Personal Customs Clearance Code) with the name and the mobile phone number.

The Customs ID Numbers (PCCC) comprises 12 digits starting with the alphabet letter P (e.g. P123123123123) and is issued by the KCS to those planning to ship personal goods into or out of Korea.

This package is suitable for overseas direct purchase e-commerce platforms that need to validate Customs Id Numbers for large number of orders on a daily basis.

해외직구 플랫폼을 운영하면서 다수의 플랫폼에서 개인통관고유부호를 제대로 수집하지 않는 경우, 개인통관고유부호 오기입, 미기입 등 불필요한 CS를 최소화 하기 위해 여러 프로그램에 적용 가능한 패키지입니다. 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.

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
{'success': False, 'customsIdNumber': '*************', 'name': '김진*', 'phone': '010-****-****', 'errors': ['납세의무자 휴대전화번호가 일치하지 않습니다.']}
>>> validate("P2200********", ['김진', '김진*'], ['010-****-****'])
{'success': True, 'customsIdNumber': '*************', 'name': '김진*', 'phone': '010-****-****', 'errors': []}
```

5. 프로젝트에 적용하기
```python
from customs_id_number import validate

validate('P123123123123', ['이름일', '이름이'], ['010-2323-2323', '010-2424-2424'], nameFilterList= ['Interpark', 'Lotteon', 'Kshopping', '11st', 'Tmon'])
```

## How it works

1. 보통 주문을 수집하는 경우 고유통관고유부호, 주문자 성명, 주문자 휴대폰번호, 수취인 성명, 수취인 휴대폰번호 이렇게 5개를 수집하는데 주문자가 본인의 개인통관고유부호를 기입하는 경우, 미기입하는 경우 휴대폰번호가 관세청에 등록되어 있는 번호와 다른 경우 오류가 발생합니다.
2. 위에 예시 처럼 매개변수는 (개인통관고유부호: str, 주문자와 수취인 성명: List[str], 휴대폰번호들: List[str], 이름필터: List[str] = []) 이렇게 네 가지이며 리스트 크기는 상관없이 모든 경우의 수로 확인합니다. 이름필터 같은 경우는 선택입니다. (사방넷 몇몇 오픈마켓에서 플랫폼 이름과 번호를 수취인명 또는 주문자명으로 등록하는 경우 대비)
3. 결과값 경우의 수<br />


## Result

- customIdNumber = o, name = [o, o], phone = [o, o]
```python
{'success': True, 'customsIdNumber': 'P21*********7', 'name': '오**', 'phone': '010-****-**72', 'errors': []}
```

- customIdNumber = o, name = [o, x], phone = [o, x]
```python
{'success': True, 'customsIdNumber': 'P21*********7', 'name': '오**', 'phone': '010-****-**72', 'errors': []}
```

- customIdNumber = o, name = [x, o], phone = [o, '']
```python
{'success': True, 'customsIdNumber': 'P21*********7', 'name': '오**', 'phone': '010-****-**72', 'errors': []}
```

- customIdNumber = o, name = ['', o], phone = [o, '']
```python
{'success': True, 'customsIdNumber': 'P21*********7', 'name': '오**', 'phone': '010-****-**72', 'errors': []}
```

- customIdNumber = '', name = ['', o], phone = [x, '']
```python
{'success': False, 'customsIdNumber': '', 'name': '', 'phone': '010-****-**72', 'errors': ['납세의무자 개인통관고유부호가 존재하지 않습니다.', '납세의무자의 휴대전화번호 확인이 불가능하기 때문에 재확인이 필요 합니다.']}
```

- customIdNumber = o, name = ['', x], phone = [o, '']
```python
{'success': False, 'customsIdNumber': 'P21*********7', 'name': '육**', 'phone': '010-****-**72', 'errors': ['입력하신 납세의무자명(육경욱)이 개인통관고유부호의 성명과 일치하지 않습니다. 납세의무자명(pltxNm)] 파라미터가 깨질경우 UTF-8로 변환하여 실행하십시오.']}
```

- customIdNumber = o, name = ['', o], phone = [x, '']
```python
{'success': False, 'customsIdNumber': 'P21*********7', 'name': '오**', 'phone': '010-****-**73', 'errors': ['납세의무자 휴대전화번호가 일치하지 않습니다.']}
```

- customIdNumber = x, name = ['', o], phone = [x, '']
```python
{'success': False, 'customsIdNumber': 'P21*********6', 'name': '오**', 'phone': '010-****-**72', 'errors': ['납세의무자 개인통관고유부호가 존재하지 않습니다.', '납세의무자의 휴대전화번호 확인이 불가능하기 때문에 재확인이 필요 합니다.']}
```

customIdNumber = o, name = ['', x], phone = [x]
```python
{'success': False, 'customsIdNumber': 'P21*********7', 'name': '육**', 'phone': '010-****-**73', 'errors': ['입력하신 납세의무자명(육경욱)이 개인통관고유부호의 성명과 일치하지 않습니다. 납세의무자명(pltxNm)] 파라미터가 깨질경우 UTF-8로 변환하여 실행하십시오.', '납세의무자 휴대전화번호가 일치하지 않습니다.']}
```