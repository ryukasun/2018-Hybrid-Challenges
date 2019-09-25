#This for the cipher technologies project
#If F is the value which represents the LSFR feedback and S is the current state of LFSR, the next state of the LFSR is computed as follows
#if the lowest bit of S is 0: S = S >> 1, 
#if the lowest bit of S is 1: S = (S >> 1) ^ F, bitwise xor = ^

#feedback value is 0x87654321
import math, binascii

#Code will take a bytearray of data, with the string name of something, apple in this example
#Code will create a keystream that is a byte array
def Crypt(data, initialValue):
    
    #data should be of type bytestring
    #initialValue will be an unsigned int, or a hexadecimal int in this case
    
    
    
    
    
    #Check parameter here to see what the value 
    print("Starting crypt")
    print("The length of the data is ", len(data))
    #print(data)
    dataByte = bytearray(data, 'utf-8')
    #print(dataByte)
    #print(len(dataByte))
    
    #dataSplit = list(data)
   # dataByteSplit = bytearray(dataSplit, 'utf-8')
    
    
   # print(dataByteSplit)
    
    dataLength = len(data)
    feedbackVal = 0x87654321 #setting the feedback value
    steps = 8 #number of steps for reading key value
    
    currentState = initialValue
    keyStream = ""
    keyStreamRev = ""
    #keyStreamVal = 0x00
    keyStreamList = []
    keyByteArray = bytearray()
    
    
    #We want to create a byte array that holds the keystream, so we can initialize a byte array an
    
    #Getting keystream
    #We want to create a bytearray that can be iterated through
    for j in range(dataLength):# will iterate for as much as length of the data
        for i in range(steps):#will iterate for the number of steps
            if(int(currentState) % 2 == 0):#if the lowest bit is 0
                currentState = currentState >> 1 #simply does a bitwise shift 
            else: # else if the lowest bit is 1 
                currentState = (currentState >> 1) ^ feedbackVal #does a bitwise shift and afterwards does an xor with the feedbackVal
            #print("Step ", i , " : " ,hex(currentState))
            
            
        
        
        #here add the code to the keystream being made
        #We want to start creating another bytearray here so that we can add things to it
        
        
        lastByte = hex(currentState % 256) #gets the hex value of the last 2 hexdigits 0xXX
        #keyStream = keyStream + "\\" + str(lastByte)
        
        #keyByteArray.extend(lastByte.encode())
        keyStream = "\\" + str(lastByte) + keyStream
        keyStreamRev = keyStreamRev + "\\" + str(lastByte)
        keyStreamList.append(currentState % 256)
        
        #keyStreamVal = keyStreamVal + (currentState % 256)*(16 ^ j)
        #print("The current keyStream is: " ,keyStream)
        #print("The current keyStreamRev is: " ,keyStreamRev)
        #print("The current keyStreamList is: " ,keyStreamList)
        #print(keyByteArray)
        #print("The current keyStreamRevByte is: " ,bytearray(keyStreamList))
        
        
        #print("The current keyStreamVal is: ", hex(keyStreamVal))
        
        
        #print("")
        
    
    #Getting inputVal
    #Encode the data as hexadecimal so it can be XOR
    b = bytearray()
    encrypt = bytearray()
    newArray = []
    
    keyByteArray.extend(keyStreamList)
    dataEncode = data.encode().hex()#encode the string data into hexadec
    
   # print("0x",dataEncode,sep="")
    b.extend(data.encode())
    #c.extend
    #print(b)
   # print(hex(b[0]^0xAC))
    #print(b[1])
    print("The keystream list is", keyStreamList)
    keyBin = binascii.hexlify(bytearray(keyStreamList))
    print("the value of keyBin is", keyBin)
    print("the value of keyByteArray is", keyByteArray)
   # print(b)
    
    
    
    
    for k in range(dataLength):
       # print((b[k] ^ keyByteArray[k]))
        #print(hex(b[k] ^ keyByteArray[k]))
        newArray.append(b[k] ^ keyByteArray[k])
        encrypt.append(dataByte[k] ^ keyByteArray[k])
        
        
        
    print("The new array of the value is ", newArray)
    print("The value of the encrypt is", encrypt)
    print("The value of this array when encoded is", bytearray(newArray))
    binAs = binascii.hexlify(encrypt)
    print("The Value of binAs", binAs)
    print("The decode of binAs is", binAs.decode())
    ggg = binAs.decode()
    print(bytes.fromhex(ggg))
    binascii.unhexlify(binAs).decode('utf-8')
   # print("The value of the decode is", binAs.decode()))
    #bytes.fromhex(binAs.decode()).decode()
    
    
    3#rint(encrypt.decode())
    #print(bytearray(newArray).decode())
    #print(encrypt.decode('ASCII'))
    #print(bytes([1,2,3,4,5]))

    
    
    #XOR the hexadecimal data with the keyStream
    
    #We want to create an XOR where we check the encoded version of our string and 
    
        
    
    
        
        
        
        
        #outputval = 0x41^0x25
        #print(hex(outputval))
        
    
    
    
    #Return a bytestring


    
    
    

    return binAs

def main():
    #Crypt("apple", 0xFFFFFFFF)
    Crypt("apple", 0x12345678)
    print("###############")
    print("")
    Crypt("\xCD\x01\xEF\xD7\x30", 0x12345678 )
    
    
    #print(hex(0xAC^0x61)) #cd
    #print(hex(0x71^0x70)) #01
    

if __name__ == "__main__":
    main()