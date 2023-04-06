

def decimal_to_roman(decimal):
    roman = ""
    while decimal >= 1000:
        roman += "M"
        decimal -= 1000
    if decimal >= 900:
        roman += "CM"
        decimal -= 900
    elif decimal >= 500:
        roman += "D"
        decimal -= 500
    elif decimal >= 400:
        roman += "CD"
        decimal -= 400
    while decimal >= 100:
        roman += "C"
        decimal -= 100
    if decimal >= 90:
        roman += "XC"
        decimal -= 90
    elif decimal >= 50:
        roman += "L"
        decimal -= 50
    elif decimal >= 40:
        roman += "XL"
        decimal -= 40
    while decimal >= 10:
        roman += "X"
        decimal -= 10
    if decimal >= 9:
        roman += "IX"
        decimal -= 9
    elif decimal >= 5:
        roman += "V"
        decimal -= 5
    elif decimal >= 4:
        roman += "IV"
        decimal -= 4
    while decimal > 0:
        roman += "I"
        decimal -= 1
    return roman

