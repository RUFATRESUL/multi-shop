


azen_eq = {
    'ü' : 'u', 'ö' : 'o', 'ğ' : 'gh', 'ş' : 'sh', 'ç' : 'ch', 'ı' : 'i', 'ə' : 'e',
    'Ü' : 'U', 'Ö' : 'O', 'Ğ' : 'Gh', 'Ş' : 'Sh', 'Ç' : 'Ch', 'İ' : 'I', 'Ə' : 'E',
}

def get_slug(text):
    result = ''
    for letter in text:
        if letter.isalnum():
            result += azen_eq.get(letter, letter)
        elif letter == ' ':
            result += '-'
    return result 


# 