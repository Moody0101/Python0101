# Gonna make another one with classes and methodes to costumize
import os

global cssFile, jsFile, htmlFile, file_name
YES = [
    'y', 'yes', 'Y', 'YES', 'Yes'
]
No = [
    'n', 'No', 'NO', 'no'
]
i = 0
html_content = [
    '<!DOCTYPE html>',
    '<html lang="en">',
    '<head>',
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<link rel="stylesheet" type="text/css" href="fontawesome/css/all.min.css">',
    '<meta http-equiv="refresh" content="">',
    '</head>',
    '<body>'
    ''
    ''
    ''
    '</body>',
    '</html>'
]
current = str(os.getcwd())
dir_ch = input('DO you want to create in new folder (y/n): --->   ')
js_boolean = input(' do you want to make a js file(y/n) : ')
if dir_ch in YES:
    folderName = input('enter the name of folder : --->   ')
    path = os.path.join(str(current) + '\\' + str(folderName))
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    print(path)
    file_name = input('enter the name of the html file to be created : -->  ')
    if js_boolean in YES:
        jsFile = file_name + '.js'
        jsF = open(jsFile, 'a')
        jsF.close()
    else:
        pass
    htmlFile = file_name + '.html'
    cssFile = file_name + '.css'
    htmlF = open(htmlFile, 'a')
    filePath = path + '\\' + htmlFile
    if os.path.exists(filePath):
        f = open(htmlFile, 'w')
        for text in html_content:
            f.write(text)
            f.write("\n")
            i += 1
            if i == 4:
                f.write('<script src=\"' + jsFile + '\"></script>')
            elif i == 5:
                f.write('<link rel=\"stylesheet\" type=\"text/css\" href=\"' + cssFile + '\">')
            elif i == 6:
                f.write('<title>' + file_name + '</title>')

    htmlF.close()
    cssF = open(cssFile, 'a')
    cssF.close()



elif dir_ch in No:

    path = str(os.getcwd())
    file_name = input('enter the name of the html file to be created : --->  ')
    if js_boolean in YES:
        jsFile = file_name + '.js'
        jsF = open(jsFile, 'a')
        jsF.close()
    else:
        pass
    htmlFile = file_name + '.html'
    cssFile = file_name + '.css'
    htmlF = open(htmlFile, 'a')
    filePath = path + '\\' + htmlFile
    if os.path.exists(filePath):
        f = open(htmlFile, 'w')
        for text in html_content:
            f.write(text)
            f.write("\n")
            i += 1
            if i == 4:
                f.write("<script src=\"" + jsFile + '"\"></script>')
            elif i == 5:
                f.write('<link rel=\"stylesheet\" type=\"text/css\" href=\"' + cssFile + '\">')
            elif i == 6:
                f.write('<title>' + file_name + '</title>')
    htmlF.close()
    cssF = open(cssFile, 'a')
    cssF.close()
