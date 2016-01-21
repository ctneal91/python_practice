class fileSystem:
    def convertTo(self):
        print('I am converting to this file system.')
    def dynamicPart(self):
        print('I am changing to a dynamic partition')
    def status(self):
        print('I am currently displaying the status of my system')
    def virutal(self):
        print('I am now a virtual file system')

class NTFS(fileSystem):
    def convertTo(self):
        super().convertTo()
        print('I have converted to NTFS filesystem')

def main():
    myFS=fileSystem()
    myFS.convertTo()

    myFS2=NTFS()
    myFS2.convertTo()

main()
