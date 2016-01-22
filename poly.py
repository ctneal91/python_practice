class network:
    def cable(self):
        print('I am the cable')
    def router(self):
        print('I am the router')
    def switch(self):
        print('I am the switch')
    def wifi(self):
        print('I am a wireless router; cable does not matter.')

class tokenRing(network):
    def cable(self):
        print('I am a token ring network cable.')
    def router(self):
        print('I am a token ring network router.')

class ethernet(network):
    def cable(self):
        print('I am an ethernet cable')
    def router(self):
        print('I am an ethernet router')
    def wifi(self):
        print('I am wifi for Mac only')

def main():
    windows=tokenRing()
    mac=ethernet()

    for obj in (windows, mac):
        obj.cable()
        obj.router()
        obj.wifi()

main()
