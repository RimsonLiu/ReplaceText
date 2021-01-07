    import os
    import codecs
    dir = 'dir'
    files = os.listdir(dir)
    for f in files:
        file = os.path.join(dir, f)
        file_object = codecs.open(file, 'r', 'utf8', errors='ignore')
        data = file_object.read()
        data = data.replace('old text',
                            'new text')
        file_object.close()

        file_object = open(file, 'wt')
        file_object.write(data)
        file_object.close()
