def main():
    try:
        f=open('filex.txt')
        x=1/0
    except ZeroDivisionError as e:
        print('division by zero')
    except FileNotFoundError as e:
        print('the file does not exist')
    except:
        print('unknown problem')


main()
