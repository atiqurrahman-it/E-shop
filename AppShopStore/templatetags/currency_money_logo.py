from django import template

register = template.Library()


@register.filter(name='currency_money')
def currency_money(taka):
    return "৳"+str(taka)
    # return "&#2547"
