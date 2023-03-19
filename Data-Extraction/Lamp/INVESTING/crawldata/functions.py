import re


# def getnum(string: str = None) -> str:
#     return float(string.rstrip("%")) if "%" in string else float(string)


def get_number(string: object = None) -> str:
    return re.sub(r"([^0-9.])", "", str(string).strip()) if string else ""


def get_char(string: object = None) -> str:
    CODE = string.replace(' - ', '_').replace('&', '_').replace('-', '_').replace(
        '(', '').replace(')', '').replace('  ', '_').replace('__', '_')
    CODEDT = CODE.split('_')
    KQ = ""
    for row in CODEDT:
        KQ = KQ + row.strip()[:1]
    return KQ.upper()


def get_code(string: object = None) -> str:
    CODE = string.replace(' ', '_').replace('&', '_').replace('.', '')
    if len(CODE) >= 20:
        CODE = CODE.split('_')[0]+get_char(CODE)
    if len(CODE.upper()) <= 20:
        return CODE.upper()
    else:
        get_code(CODE.upper())
