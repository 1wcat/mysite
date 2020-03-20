from jinja2 import Template

def getHtml():
    with open('items.html') as f:
        s = f.read()
    return s

def main():
    item_list = [
        { 'name': 'apple', 'count': 50},
        { 'name': 'papaya', 'count': 90},
        { 'name': 'banana', 'count': 20}
    ]
    
    tmpl = Template(getHtml())
    print(tmpl.render({'items': item_list}))

main()