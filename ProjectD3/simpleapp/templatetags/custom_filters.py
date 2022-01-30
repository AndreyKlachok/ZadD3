from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return str(value) * arg

@register.filter(name='censor')
def censor(value):
    censor_list = ['буй',
                   'езда',
                   'шопа']
    value1 = (str(value)).split()
    for i in censor_list:
        for j in value1:
            if j == i:
                value1.remove(i)
    value = ' '.join(value1)
    return str(value)