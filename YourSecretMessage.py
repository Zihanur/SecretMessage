alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = 5
newMessage = ''

message = input("Enter any letter: ")
password = int(input("Enter any password: "))
for charter in message:
    if charter in alphabet:
        possition = alphabet.find(charter)
        newPossition = (possition+key)%26
        newCharter = alphabet[newPossition]
        newMessage = newMessage+newCharter
    else:
        newMessage = newMessage+charter

print("Your secret code: ", newMessage)