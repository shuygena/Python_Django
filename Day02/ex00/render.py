import sys, os, re

try:
    import settings
except Exception:
    print("Error: can't import settings.py")

def replace_vars(html, sets):
    if "title" in sets: 
        html = re.sub("{title}", sets["title"], html)
    if "name" in sets:
        html = re.sub("{name}", sets["name"], html)
    if "surname" in sets:
        html = re.sub("{surname}", sets["surname"], html)
    if "internship" in sets:
        html = re.sub("{internship}", sets["internship"], html)
    if "location" in sets: 
        html = re.sub("{location}", sets["location"], html)
    return(html)

def main():
    if len(sys.argv) != 2:
        print("Error: wrong number of arguments")
        sys.exit()
    sets = vars(settings)
    if sys.argv[1] != "myCV.template":
        print("Error: bad filename")
        sys.exit()
    try:
        template = open(sys.argv[1], "r")
    except Exception:
        print("Error: can't open .template file")
        sys.exit()
    html = template.read()
    edited_html = replace_vars(html, sets)
    file_html = open("myCV.html", "w+")
    file_html.write(edited_html)

main()
    
