# /package/customs_id_number.py
import configparser
from re import T
import requests
import xml.etree.ElementTree as ET
from utils.mobile_number_format import addHyphen, removeHyphen

config = configparser.ConfigParser()
config.read('unipass.ini')
UNIPASS_API_KEY = config['DEFAULT']['UNIPASS_API_KEY']
print(UNIPASS_API_KEY)


def api_request(customsIdNumber: str, name: str, phone: str):
    if len(customsIdNumber) != 13 or len(name) < 2 or len(phone) < 9:
        return {'success': False, 'errors': ['정보가 정확하게 입력되지 않았습니다']}
    requestURL = f'https://unipass.customs.go.kr:38010/ext/rest/persEcmQry/retrievePersEcm?crkyCn={UNIPASS_API_KEY}&persEcm={customsIdNumber}&pltxNm={name}&cralTelno={removeHyphen(phone)}'
    response = requests.get(requestURL)
    # print(response.text)
    # if response.text == '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><persEcmQryRtnVo><tCnt>1</tCnt></persEcmQryRtnVo>':
    #    return {'success': True, 'error': []}
    response_element = ET.fromstring(response.text)
    resultString = response_element.find('tCnt').text
    errors = []
    if resultString == '1':
        return {'success': True, 'errors': []}
    else:
        # print(response.text)
        for reason in response_element.findall(
                'persEcmQryRtnErrInfoVo'):
            errors.append(reason.find('errMsgCn').text)
        return {'success': False, 'errors': errors}
    print(errors)
    # for child in response_element:
    #     print(child.tag, child.attrib, child.text)

# def mobileNumberValidation(phone1: str, phone2: str = ""):
#     if phone


def validate(customsIdNumber: str, name1: str, phone1: str, name2: str = "", phone2: str = ""):
    finalName = ''
    finalPhone = ''
    result = {}
    result = api_request(customsIdNumber, name1, phone1)
    if result['success']:
        return {'success': True, 'customsIdNumber': customsIdNumber, 'name': name1, 'phone': addHyphen(phone1), 'errors': result['errors']}
    else:
        if '성명' not in ' '.join(result['errors']):
            finalName = name1
        if '휴대전화번호' not in ' '.join(result['errors']):
            finalPhone = addHyphen(phone1)

    if api_request(customsIdNumber, name1, phone2)['success']:
        return {'success': True, 'customsIdNumber': customsIdNumber, 'name': name2, 'phone': addHyphen(phone1), 'errors': result['errors']}
    else:
        if '성명' not in ' '.join(result['errors']):
            finalName = name2
        if '휴대전화번호' not in ' '.join(result['errors']):
            finalPhone = addHyphen(phone1)

    if api_request(customsIdNumber, name1, phone2)['success']:
        return {'success': True, 'customsIdNumber': customsIdNumber, 'name': name1, 'phone': addHyphen(phone2), 'errors': result['errors']}
    else:
        if '성명' not in ' '.join(result['errors']):
            finalName = name2
        if '휴대전화번호' not in ' '.join(result['errors']):
            finalPhone = addHyphen(phone2)

    if api_request(customsIdNumber, name2, phone2)['success']:
        return {'success': True, 'customsIdNumber': customsIdNumber, 'name': name2, 'phone': addHyphen(phone2), 'errors': result['errors']}
    else:
        if '성명' not in ' '.join(result['errors']):
            finalName = name2
        if '휴대전화번호' not in ' '.join(result['errors']):
            finalPhone = addHyphen(phone2)

    return {'success': False, 'customsIdNumber': customsIdNumber, 'name': finalName, 'phone': finalPhone, 'errors': result['errors']}


print(validate("P123", '공경섭', '010-6878-3628'))
print(validate("P220003429872", '공경섭', '010-878-3628'))
print(validate("P220003429872", '김진숙', '010-4524-7875'))
print(validate("P220003429872", '김진', '010-4524-7875'))
print(validate("P220003429872", '김진', '010-4524-7873'))
