from hashlib import sha256

class hasher:
    def __init__ (self):
        self.inputString = ""
        self.hashString = ""

    def setInputString (self, input):
        self.inputString = input

    def __getSHA256 (self, input):
        messageDigest = sha256()
        encodedInput = input.encode('utf-8')
        messageDigest.update(encodedInput)
        return messageDigest.hexdigest()
    
    def hashConvert (self):
        self.hashString = self.__getSHA256(self.inputString)
    
    def getInputString (self):
        return self.inputString
    
    def getHashString (self):
        return self.hashString
    

hasherTest = hasher()
print("Created Hasher")
hasherTest.setInputString("Oliver Cheung, 213213213, December 19 2004, Biden")
hasherTest.hashConvert()
print(str(hasherTest.getInputString()) + " --> " + str(hasherTest.getHashString()))