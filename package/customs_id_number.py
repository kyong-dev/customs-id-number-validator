# /package/customs_id_number.py

from utils.mobile_number_format import addHyphen, removeHyphen


def validate(customsIdNumber: str, name1: str, phone1: str, name2: str = "", phone2: str = ""):
    print(removeHyphen(phone1))
    print(addHyphen(phone1))


validate("P123", '공경섭', '010-6878-3628')
validate("P123", '공경섭', '010-878-3628')
