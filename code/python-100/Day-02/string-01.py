import string

s = 'The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))

values = {'var': 'foo'}

t = string.Template("""
Variable   : $var
Escape     : $$
Variable in text:${var}iable
""")
print('Template:',t.substitute(values))

s = """
Variable : %(var)s
Escape   : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION',s % values)

s1 = """
Variable : {var}
Escape   : {{}}
Variable in text: {var}iable
"""

print('FORMAT:',s1.format(**values))

# 高级模板

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
    delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notunderscored
'''

d = {
    'with_underscore':'replaced',
    'notunderscored':'not replaced'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))

