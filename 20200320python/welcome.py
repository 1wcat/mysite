from jinja2 import Template

def welcomeHtml():
    with open('welcome.html') as f:
        s = f.read()
    return s

def main():
    user = { 'name': 'Alice', 'likes': 100}
    user2 = { 'name': 'Blurry', 'likes': 250}
    
    tmpl = Template(welcomeHtml())
    print(tmpl.render(user))
    print(tmpl.render(user2))

main()