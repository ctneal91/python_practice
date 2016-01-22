import sys
import os
import datetime

def main():
    print("version {}.{}.{}".format(*sys.version_info))
    print(sys.platform)

    print(os.name)
    print(os.getenv("userdomain"))
    print(os.getcwd())

    now = datetime.datetime.now()

    print(now)

    print(now.year,now.month,now.day,now.hour)
main()
