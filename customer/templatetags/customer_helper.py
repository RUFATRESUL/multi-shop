from django import template

register = template.Library()

symbols = {'USD':'$','EUR':'€','TRY':'₺','AZN':'₼'}
@register.simple_tag
def get_price_text(request,price):
    currency = request.session.get('currency','USD')
    currency_ratio = request.session.get('currency_ratio',1)
    symbol = symbols[currency]
    result_price = round(price*currency_ratio,2)
    return f'{result_price:,} {symbol}'