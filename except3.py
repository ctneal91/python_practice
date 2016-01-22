def main():
    try:
        fh=open('file3.txt')
    except IOError as e:
        print('could not open this file: ', e)
    else:
        for line in fh: print(line.strip())

main()
