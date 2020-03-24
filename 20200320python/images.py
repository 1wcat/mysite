from jinja2 import Template

def getHtml():
    with open('images.html') as f:
        s = f.read()
    return s

def main():
    image_list = [
        { 'title': 'picture1', 'url': "https://i.pinimg.com/736x/11/2b/74/112b746a2182417b2a947d949798c968.jpg"},
        { 'title': 'picture2', 'url': "https://www.serebii.net/swordshield/pokemon/778.png"},
        { 'title': 'picture3', 'url': "https://cdn.shopify.com/s/files/1/0217/9998/products/african-gyename-mask.jpg?v=1492402709"}
    ]
      
    tmpl = Template(getHtml())
    print(tmpl.render({'image': images_list}))

main()