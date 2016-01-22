try:
    fh=open('filename')
except IOError as e:
        print(e)
    else:
        for 1 in fh:print(1)
