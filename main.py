import numpy as np

# Определяем матрицу K
K = np.array([[10, 8, 3],
              [2, 19, 5],
              [5, 7, 22]])

# Определяем модуль
mod = 37

# Функция для нахождения обратного элемента по модулю
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Функция для вычисления обратной матрицы
def inverse_matrix(K, mod):
    det = int(np.round(np.linalg.det(K))) % mod
    det_inv = mod_inverse(det, mod)
    adjugate = np.round(det * np.linalg.inv(K)).astype(int) % mod
    inv_K = (det_inv * adjugate) % mod
    return inv_K

# Вычисляем обратную матрицу
K_inv = inverse_matrix(K, mod)
print("Обратная матрица K^-1:\n", K_inv)

# Определяем алфавит
alphabet = {chr(i + 1040): i + 10 for i in range(33)}  # Русский алфавит
alphabet.update({str(i): i for i in range(10)})  # Цифры
alphabet['.'] = 33
alphabet[','] = 34
alphabet[' '] = 35
alphabet['?'] = 36

# Создаем обратный словарь для декодирования
reverse_alphabet = {v: k for k, v in alphabet.items()}

# Функция для шифрования сообщения
def encrypt(message, K, mod):
    message_vector = [alphabet[char] for char in message]
    # Дополняем вектор до кратности 3
    while len(message_vector) % 3 != 0:
        message_vector.append(35)  # Пробел
    encrypted_vector = []
    for i in range(0, len(message_vector), 3):
        block = np.array(message_vector[i:i+3])
        encrypted_block = np.dot(K, block) % mod
        encrypted_vector.extend(encrypted_block)
    return encrypted_vector

# Функция для расшифровки сообщения
def decrypt(encrypted_vector, K_inv, mod):
    decrypted_vector = []
    for i in range(0, len(encrypted_vector), 3):
        block = np.array(encrypted_vector[i:i+3])
        decrypted_block = np.dot(K_inv, block) % mod
        decrypted_vector.extend(decrypted_block)
    return decrypted_vector

# Шифруем фразу «НЕПЕТЯЯЯН»
message = "НЕПЕТЯЯЯН"
encrypted_vector = encrypt(message, K, mod)
print("Зашифрованный текст:", encrypted_vector)

# Расшифровываем шифротекст
decrypted_vector = decrypt(encrypted_vector, K_inv, mod)
decrypted_message = ''.join([reverse_alphabet[int(x)] for x in decrypted_vector])
print("Расшифрованный текст:", decrypted_message)
