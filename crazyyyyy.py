import numpy as np

# Определяем матрицу K
K = np.array([[10, 8, 3],
              [2, 19, 5],
              [5, 7, 22]])

# Определяем модуль
mod = 37

# Создаем алфавит
alphabet = {chr(i + 1040): i + 10 for i in range(33)}  # Русский алфавит
alphabet.update({str(i): i for i in range(10)})  # Цифры
alphabet['.'] = 33
alphabet[','] = 34
alphabet[' '] = 35
alphabet['?'] = 36

# Создаем обратный алфавит для дешифрования
reverse_alphabet = {v: k for k, v in alphabet.items()}

def encrypt(word):
    encrypted = []
    for char in word:
        if char in alphabet:
            encrypted.append(alphabet[char])
        else:
            encrypted.append(char)  # Если символ не в алфавите, оставляем его без изменений
    return encrypted

def decrypt(encrypted_list):
    decrypted = []
    for num in encrypted_list:
        if num in reverse_alphabet:
            decrypted.append(reverse_alphabet[num])
        else:
            decrypted.append(num)  # Если число не в обратном алфавите, оставляем его без изменений
    return ''.join(decrypted)

# Шифруем слово
word_to_encrypt = "НЕПЕТЯЯЯН"
encrypted_word = encrypt(word_to_encrypt)
print("Зашифрованное слово:", encrypted_word, encrypt('ДИССОНАНС'))

# Дешифруем слово
decrypted_word = decrypt(encrypted_word)
print("Расшифрованное слово:", decrypted_word, decrypt('ДИССОНАНС'))

def list_to_matrix(lst):
    if len(lst) != 9:
        raise ValueError("Список должен содержать ровно 9 чисел.")
    
    # Преобразуем список в матрицу 3x3
    matrix = []
    for i in range(3):
        row = lst[i*3:(i+1)*3]  # Берем срез списка для каждой строки
        matrix.append(row)
    
    return matrix

# Пример использования
numbers = encrypt('ДИССОНАНС')
matrix = list_to_matrix(numbers)

# Вывод матрицы
for row in matrix:
    print(row)

def split_into_blocks(lst):
    blocks = []
    
    # Проходим по списку с шагом 3
    for i in range(0, len(lst), 3):
        block = lst[i:i+3]
        
        # Если блок содержит меньше 3 элементов, дополняем его до 3 элементами 35
        while len(block) < 3:
            block.append(35)
        
        # Добавляем блок в список блоков
        blocks.append(block)
    
    return blocks

def multiply_blocks(blocks, matrix_3x3):
    results = []
    
    for block in blocks:
        # Преобразуем блок в numpy массив и умножаем на заданную матрицу
        block_matrix = np.array(block).reshape(3, 1)  # Преобразуем в 3x1
        result = np.dot(matrix_3x3, block_matrix)
        
        # Заменяем каждый элемент результата на остаток от деления на 37
        result = result % 37
        
        results.append(result)
    
    return results

# Пример использования
blocks = split_into_blocks(encrypted_word)

# Умножаем блоки на матрицу
results = multiply_blocks(blocks, matrix)

# Вывод результатов
for i, result in enumerate(results):
    print(f"Результат умножения блока {i+1} и остатка от деления на 37:", result.flatten())
