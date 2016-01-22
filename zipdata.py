import zipfile

fh = zipfile.ZipFile('mydata.zip', 'w')

fh.write('file1.txt')
fh.write('newfile.txt','bigfile.txt','newbig.txt')

fh.close()


#Tuesday: 830 - 445, 8.75
#Wednesday: 815 - 415, 8
#Thursday: 820 - 420 with 30 min lunch, 7.5
#Friday: 845 - 5, 8.25
