# Because python has first-class functions they can
# be used to emulate switch/case statement.

def dispatch_if(operator, x, y):
     """docstring for dispatch_if"""
     if operator == 'add':
         return x + y
     elif operator == 'sub':
         return x - y
     elif operator == 'mul':
         return x * y
     elif operator == 'div':
         return x / y
     else:
         return None


def dispatch_dict(operator, x, y):
    """docstring for dispatch_dict"""
    return {
            'add' : lambda: x + y,
            'sub' : lambda: x - y,
            'mul' : lambda: x * y,
            'div' : lambda: x / y,
            }.get(operator, lambda:None)()


print(dispatch_if('mul', 2, 8))
print(dispatch_dict('mul',2, 8))

print(dispatch_if('unknow', 2, 8))
print(dispatch_dict('unknow', 2, 8))
