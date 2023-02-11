import re

def link_from_hastags(str):
    return re.sub(r'#(\w+)','<a href=""/>#\\1</a>',str)

print(link_from_hastags("ok je vais #bien"))