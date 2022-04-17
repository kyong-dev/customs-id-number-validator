def removeHyphen(phoneNumber: str):
    return phoneNumber.replace("-", "")


def addHyphen(phoneNumber: str):
    phoneNumber = removeHyphen(phoneNumber)
    phoneNumWithHyphen = f"{phoneNumber[0:-8]}-{phoneNumber[-8:-4]}-{phoneNumber[-4:]}"
    # if the phone number has 10 digits and starts with 01
    if phoneNumber[0:-8] == "01":
        phoneNumWithHyphen = f"{phoneNumber[0:-7]}-{phoneNumber[-7:-4]}-{phoneNumber[-4:]}"

    return phoneNumWithHyphen
