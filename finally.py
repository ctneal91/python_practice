def main():

    counter = 0
    try:
        fh=open("filex.txt")
        for line in fh: print(line.strip())
    except:
        counter += 1
        pass
    finally:
        print("All work was done")
        print
        print("There were %d errors" % counter)

main()
