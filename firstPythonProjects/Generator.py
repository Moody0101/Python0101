import os

global j, indexCount


class fileList:
    """
this class is used to find files in a specified path, that has a specified extension
    """

    def __init__(self, path=None):
        self.fileList = list()

    def __str__(self):
        return str(self.fileList)

    def generator(self, path, ext=None):
        ext_format = ['.css', '.html', '.js', '.py']
        for i in os.scandir(path):
            if ext is not None:
                if i.name.endswith(ext):
                    song = i.name[:-4]
                    self.fileList.append(song)
            else:
                if not i.name.endswith((ext_format[0], ext_format[1], ext_format[2])):
                    if not i.name.startswith('.'):
                        song = i.name
                        self.fileList.append(song)
        return self.fileList


count = 0
html_content = [
    '<!DOCTYPE html>',
    '<html lang="en">',
    '<head>',
    '<style>'
    'audio {',
    'outline: none;',
    'background: none;',
    'display: block;',
    '}',
    'body' + '{',
    'padding: 0;',
    'margin: 0;',
    'background-image: url("../Images/Bts.jpg");',
    'background-size: cover;',
    'background-repeat: no - repeat;',
    'background-position: center;',
    'background-attachment: fixed;',
    '}',
    '.div' + '{',
    'background-color: white;',
    'height: 14px;',
    'align-items: center;',
    'border-top: 3px solid red;',
    '}',
    '.div, #inner-div, section {',
    'display: flex;',
    'justify-content: center;',
    'padding: 30px 0;',
    '}',
    'section{',
    "background-color: rgba(0, 0, 0, 10 %);",
    "z-index: 1;",
    '}',
    'img{',
    'border - radius: 10px;',
    'z-index: 999;',
    'opacity: 1;',
    'box-shadow: 20px 10px 0 -1px rgba(0, 0, 0, 50 %);',
    '}',
    'h3{',
    'font-family: sans - serif;',
    'font-weight: 400;',
    'margin: 10px;',
    'margin-right: 20px;',
    'text-align: center;',
    'cursor: mouse;',
    '}', '</style>',

    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<link rel="stylesheet" type="text/css" href="fontawesome/css/all.min.css">',
    '<meta http-equiv="refresh" content="">',
    '</head>',
    '<body>'
    '<section>',
    '<div id="inner-div">',
    '<img src="">',
    '</div>',
    '</section>',
    '</body>',
    '</html>',
]
albumList = fileList()
albumList.generator('../btsWebSite')
imageList = fileList()
imageList.generator('Images', '.jpg')
albums = albumList.fileList
albums.remove('Images')
albums.remove('Generator.py')
images = imageList.fileList
images.remove('Bts')
print(albums)
print(images)
for i in albums:  # for every file in the current dir
    j = 0
    count = 0
    os.chdir(
        os.path.abspath("C:\\Users\\pc\\Desktop\\My projects\\btsWebSite" + "\\" + str(i)))  # the change the dir there
    filename = str(i) + '.html'  # the file I wanna make in every  dir in the root
    filePath = str(i) + '.html'
    if not os.path.exists(filePath):  # checking if it exists
        f = open(filename, 'w')
        for text in html_content:  # if it exists write in it the content line by line
            f.write(text)
            f.write("\n")
            j += 1  # check the number of lines written
            if j > len(html_content) - 3:  # reaching this line, write this
                songNames = fileList()
                indexCount = 0
                songs = songNames.generator("C:\\Users\\pc\\Desktop\\My projects\\btsWebSite" + "\\" + str(i), ".mp3")
                while count < len(songs):
                    f.write('<div class="div"><h3>' + songs[indexCount] + '</h3><audio src="' + songs[
                        indexCount] + '.mp3" controls>  </audio></div>')
                    f.write('\n')
                    indexCount += 1
                    j += 1
                    count += 1
                else:
                    pass

        f.close()
