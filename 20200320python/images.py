from jinja2 import Template

def getHtml():
    with open('images.html') as f:
        s = f.read()
    return s

def main():
    item_list = [
        { 'title': 'mountain1', 'url': "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTEVahhGSoA4A4OIwF-0BPv0S4VOcJlW6XzdOx6sE6f7p_-ZOK9"},
    ]
    
    tmpl = Template(getHtml())
    print(tmpl.render({'image': images_list}))

main()