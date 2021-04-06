
p = 11
q = 13
n = p * q
phi_n = (p-1) * (q-1)

e = 7

d = 0
mod = 0

while True:
    d += 1
    mod = (e * d) % phi_n
    if mod == 1:
        break

# Encryption
# C = P^e mod n

plain = "Hello World"
plain_list = [ord(x) for x in plain]
# for x in plain:
#     plain_list.append(ord(x))
# ord = 숫자를 아스키코드로

cipher = []
for i in plain_list:
    x = (i ** e) % n
# **는 제곱을 의미
    cipher.append(int(x))

# Decryption
# P = C^d mod n

decrypted = []
for i in cipher:
    x = i ** d % n
    decrypted.append(int(x))

print('plain text', plain_list)
print('cipher text', cipher)
print('decrypted text', decrypted)

decrypted_text = ''.join(chr(x) for x in decrypted)
# chr = 아스키코드를 문자로
# join = 문자열로 붙여서 출력하게 하는 함수

print(decrypted_text)