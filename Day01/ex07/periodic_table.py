import sys

def parse():
    f = open("periodic_table.txt")
    elems_list = list()
    for line in f:
        elem = list()
        elem.append(((line.split('='))[0]).strip())
        for settings in line.split(","):
            if settings.find("\n") != -1:
                elem.append(settings[settings.find(":") + 1:-1])
            else:
                elem.append(settings[settings.find(":") + 1:])
        elems_list.append(elem)
    return(elems_list)

def get_color(num):
    mediumorchid = [2, 10, 18, 36, 54, 86, 118]
    green = [13, 31, 49, 50, 81, 82, 83, 113, 114, 115, 116]
    mediumpurple = [1, 6, 7, 8, 15, 16, 34]
    purple = [9, 17, 35, 53, 85, 117]
    skyblue = [5, 14, 32, 33, 51, 52, 84]
    orange = [4, 12, 20, 38, 56, 88]
    tomato = [3, 11, 19, 37, 55, 87]
    if num in mediumorchid:
        return "mediumorchid"
    if num in green:
        return "green"
    if num in mediumpurple:
        return "mediumpurple"
    if num in purple:
        return "purple"
    if num in skyblue:
        return "skyblue"
    if num in orange:
        return "orange"
    if num in tomato:
        return "tomato"
    return "yellow"

def get_html():
    parse()
    header = """
    <!DOCTYPE html>
        <html lang="en">
            <head> 
            <meta charset="UTF-8">
            <title> Periodic Mendeleev's Table </title>
               <style>
            h4{
                text-align: center;
                font-size: 14px
            }
            ul{
                padding-left: 0
            }
            table{
            }
            li{
                list-style-type: none;
            }
            td{
                width: 120px;
                height: 120px;
                padding: 0;
                border:1px solid;
                display: inline-block;
                font-size: 12px;
                margin: 2px;
            }
        </style>
        </head>
        <body>
        <table>
        """
    table = parse()
    lim = True
    pos = 0
    for elem in table:
        if (lim == True):
            header += """
            <tr>
            """
            lim = False
        prev_pos = pos
        pos = int(elem[1])
        dif = pos - prev_pos
        while (dif > 1):
            header += """
            <td style="background-color: white; border-color: white"></td>
            """
            dif = dif - 1
        header += """
        <td style="background-color: """ + get_color(int(elem[2])) +""" ">
        <h4>""" + elem[0] + """</h4>
        <ul>
            <li>""" + "No " + elem[2] + """ </li>
                <li>""" + elem[3] + """ </li>
                <li>""" + elem[4] + """ </li>
                <li>""" + elem[5] + """ </li>
            </ul>
            </td>"""
        if (pos == 17):
            lim = True
            header += """
            </tr>
            """
    header +="""
    </table>
    </body>
    </html>"""
    my_file = open("periodic_table.html", "w+")
    my_file.write(header)
    my_file.close()

if __name__ == '__main__':
    get_html()
    #parse()