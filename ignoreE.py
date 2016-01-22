def main():
    try:
        fh=open('filex.txt')
        for line in fh: print(line.strip())
    except:
        pass

main()
