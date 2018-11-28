from jinja2 import Template


template = Template('Hello {{ name }}!')
template.render(name = 'World')


from jinja2 import Environment, PackageLoader

env =Environment(loader=PackageLoader('yourapplication','templates'))

template = env.get_template('mytemplate.html')

print template.render(the='variables',go='here')