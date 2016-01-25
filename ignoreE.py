def main():
    try:
        fh=open('filex.txt')
        print("file has been opened")
        print()
        for line in fh: print(line.strip())
    except:
        pass

main()
