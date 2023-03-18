def getnum(string: str = None) -> str:
    return float(string.rstrip("%")) if "%" in string else float(string)
