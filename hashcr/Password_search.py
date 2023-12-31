import hashlib


def searchWord(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def checkPass(target_hash, commonPassword):
    for i in commonPassword:
        if hashlib.sha256(i.encode()).hexdigest() == target_hash:
            return i
        elif hashlib.sha256(i.upper().encode()).hexdigest() == target_hash:
            return i.upper()
        elif hashlib.sha256(i.lower().encode()).hexdigest() == target_hash:
            return i.lower()
        elif hashlib.sha256(i.capitalize().encode()).hexdigest() == target_hash:
            return i.capitalize()
    else:
        return None
    
if __name__ == "__main__":
    target_hash = input('Enter the hashcode\n')
    filePath = input('Enter the file path of the dictionary\n')
    commonPassword = searchWord(filePath)
    cracked_password = checkPass(target_hash, commonPassword)
    if cracked_password:
        print('Password is:\n', cracked_password)
    else:
        print(" Password not found")

    
