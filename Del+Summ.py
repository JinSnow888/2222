"""
Main
"""
def absum(a, b):   
    '''Сумма a b'''
    return(a + b)

def abdelen(a, b):
    '''Деление a b'''
    return(a / b)

RESULT = abdelen(absum(10, 20), absum(1, 2)) # Деление двух сумм

print(RESULT)
