import hashlib 

secret_code = 0

while True:
    secret_key = 'iwrupvqb' + str(secret_code)
    result = hashlib.md5(secret_key.encode()) 
    answer = result.hexdigest()
    if answer[0:6] == '000000':
        break
    secret_code += 1
print('The Secret Code', secret_code) 
print('The Secret Answer', secret_key)
print('The MD5 Hash Code ', answer)