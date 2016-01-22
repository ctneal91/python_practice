import sys

print("script name is", sys.argv[0])

try:
    print("script argument passed is ",sys.argv[1])

except:
    print("there are no more arguments passed")
