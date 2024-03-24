import math

#-----------------------------------------------------------------------------------------------------------------------#

# Function that perfroms bit rotation to the right
# 
# Takes as an input:
#   number - decimal number (int)
#   numberOfRotations - number of bits to rotate by (int)
#   bitLength - number of bits we want to use to represent the number in binary (int)
# Returns:
#   result - result of rotation (int)

def ROR(number, numberOfRotations, bitLength):
    binaryNumber = bin(number)[2:].zfill(bitLength)
    rotatedNumber = binaryNumber[-(numberOfRotations % bitLength):] + binaryNumber[:-(numberOfRotations % bitLength)]
    result = int(rotatedNumber, 2)
    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that perfroms bit rotation to the left
# 
# Takes as an input:
#   number - decimal number (int)
#   numberOfRotations - number of bits to rotate by (int)
#   bitLength - number of bits we want to use to represent the number in binary (int)
# Returns:
#   result - result of rotation (int)

def ROL(number, numberOfRotations, bitLength):
    binaryNumber = bin(number)[2:].zfill(bitLength)
    rotatedNumber = binaryNumber[(numberOfRotations % bitLength):] + binaryNumber[:(numberOfRotations % bitLength)]
    result = int(rotatedNumber, 2)
    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that perfroms permutation q0
# 
# Takes as an input:
#   number - decimal number (int)
# Returns:
#   result - result of permutation q0 (int)

def q0(number):
    t0 = [8, 1, 7, 13, 6, 15, 3, 2, 0, 11, 5, 9, 14, 12, 10, 4]
    t1 = [14, 12, 11, 8, 1, 2, 3, 5, 15, 4, 10, 6, 7, 0, 9, 13]
    t2 = [11, 10, 5, 14, 6, 13, 9, 0, 12, 8, 15, 3, 2, 4, 7, 1]
    t3 = [13, 7, 15, 4, 1, 2, 6, 14, 9, 11, 3, 0, 8, 5, 12, 10]
    
    a0 = int(number / 16)
    b0 = int(number % 16)

    a1 = a0 ^ b0
    b1 = ((a0 ^ ROR(b0, 1, 4)) ^ (8 * a0)) % 16
    
    a2 = t0[a1]
    b2 = t1[b1]
    
    a3 = a2 ^ b2
    b3 = ((a2 ^ ROR(b2, 1, 4)) ^ (8 * a2)) % 16

    a4 = t2[a3]
    b4 = t3[b3]

    result = 16 * b4 + a4

    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that perfroms permutation q1
# 
# Takes as an input:
#   number - decimal number (int)
# Returns:
#   result - result of permutation q1 (int)

def q1(number):
    t0 = [2, 8, 11, 13, 15, 7, 6, 14, 3, 1, 9, 4, 0, 10, 12, 5]
    t1 = [1, 14, 2, 11, 4, 12, 3, 7, 6, 13, 10, 5, 15, 9, 0, 8]
    t2 = [4, 12, 7, 5, 1, 6, 9, 10, 0, 14, 13, 8, 2, 11, 3, 15]
    t3 = [11, 9, 5, 1, 12, 3, 13, 14, 6, 4, 7, 15, 2, 0, 8, 10]
    
    a0 = int(number / 16)
    b0 = int(number % 16)

    a1 = a0 ^ b0
    b1 = ((a0 ^ ROR(b0, 1, 4)) ^ (8 * a0)) % 16
    
    a2 = t0[a1]
    b2 = t1[b1]
    
    a3 = a2 ^ b2
    b3 = ((a2 ^ ROR(b2, 1, 4)) ^ (8 * a2)) % 16

    a4 = t2[a3]
    b4 = t3[b3]

    result = 16 * b4 + a4

    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that formats the key to one of the supported lengths: 128-bit, 192-bit or 256-bit
# 
# Takes as an input:
#   raw_key - raw string to be formatted to key (hex in string)
# Returns:
#   key - result of formatting (binary in string)

def format_Key(raw_key):
    key = bin(int(raw_key, 16))[2:].zfill(len(raw_key)*4)
    if (len(key) % 8 != 0):
        key = "0" * (8 - (len(key) % 8)) + key

    if (len(key) > 256 ):
        key = key[:256]
    elif (256 > len(key) > 192):
        for i in range (int(((256 - len(key)) / 8))):
            key += "00000000"
    elif (192 > len(key) > 128):
        for i in range (int(((192 - len(key)) / 8))):
            key += "00000000"
    else:
        for i in range (int(((128 - len(key)) / 8))):
            key += "00000000"
    
    return key

#-----------------------------------------------------------------------------------------------------------------------#

# Function that converts text into a hexadecimal string
# 
# Takes as an input:
#   text - string containing text to be converted (string)
# Returns:
#   result - result of conversion (hex in string)

def text_To_Hex(text):
    result = ""

    for char in text:
        number = ord(char)
        result = result + hex(number)[2:].zfill(2)

    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that converts hexadecimal string into text
# 
# Takes as an input:
#   hex_string - string containing text to be converted (hex in string)
# Returns:
#   result - result of conversion (string)

def hex_To_Text(hex_string):
    result = ""

    for i in range(0, len(hex_string), 2):
        hex_pair = hex_string[i:i+2]
        character = chr(int(hex_pair, 16))
        result += character

    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that is responsible for providing Me, Mo, S for generating subkeys
# 
# Takes as an input:
#   key - string containing key (binary in string)
# Returns:
#   Me - list of 32-bit words (binary in string)
#   Mo - list of 32-bit words (binary in string)
#   S - list of 32-bit words (binary in string)

def key_Schedule(key):
    k = int(len(key) / 64)
    m = [0] * 8 * k
    M = [0] * 2 * k
    for i in range (int(len(key) / 8)):
        m[i] = key[8 * i : 8 * (i + 1)]
    
    for i in range (len(M)):
        temp = 0
        for j in range (4):
            temp += int(m[(4 * i) + j], 2) * ( 2 ** (8 * j))
        M[i] = temp

    Me = [bin(M[i])[2:].zfill(32) for i in range (0, len(M), 2)]
    Mo = [bin(M[i])[2:].zfill(32) for i in range (1, len(M), 2)]

    RS = [[1, 164, 85, 135, 90, 88, 219, 158],
          [164, 86, 130, 243, 30, 198, 104, 229],
          [2, 161, 252, 193, 71, 174, 61, 25],
          [164, 85, 135, 90, 88, 219, 158, 3]]
    
    S = []
    Si = []

    for i in range(k):
        result = GF_256_multiply_Matrices(RS, [[int(m[8*i], 2)], 
                                                  [int(m[8*i+1], 2)], 
                                                  [int(m[8*i+2], 2)], 
                                                  [int(m[8*i+3], 2)], 
                                                  [int(m[8*i+4], 2)], 
                                                  [int(m[8*i+5], 2)], 
                                                  [int(m[8*i+6], 2)], 
                                                  [int(m[8*i+7], 2)]], 0x14D)
        
        Si.append(bin(result[3][0])[2:].zfill(8) + 
                  bin(result[2][0])[2:].zfill(8) + 
                  bin(result[1][0])[2:].zfill(8) + 
                  bin(result[0][0])[2:].zfill(8))
    
    for i in range(k):
        S.append(Si[k-i-1])

    return Me, Mo, S
        
#-----------------------------------------------------------------------------------------------------------------------#

# Function that performs matrix multiplication in GF(256) with given primitive polynomial: 
#
# Note:
#       x^8 + x^6 + x^3 + x^2 + 1 is the primitive polynomial for key schedule (0x14D)
#       x^8 + x^6 + x^5 + x^3 + 1 is the primitive polynomial for g function   (0x169)
# 
# Takes as an input:
#   matrix1 - 1st matrix (list of lists of int)
#   matrix2 - 2nd matrix (list of lists of int)
#   polynomial - primitive polynomial of the GF(256) that we work on (hex in int)
# Returns:
#   result - result of matrix multiplication (int)

def GF_256_multiply_Matrices(matrix1, matrix2, polynomial):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Cannot multiply matrices.")

    result = [[0] * cols2 for i in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] ^= GF_256_multiply(matrix1[i][k], matrix2[k][j], polynomial)

    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that performs multiplication in GF(256) with primitive polynomial:
#
# Note:
#       x^8 + x^6 + x^3 + x^2 + 1 is the primitive polynomial for key schedule (0x14D)
#       x^8 + x^6 + x^5 + x^3 + 1 is the primitive polynomial for g function   (0x169)
# 
# Takes as an input:
#   a - 1st number (int)
#   b - 2nd number (int)
#   polynomial - primitive polynomial of the GF(256) that we work on (hex in int)
# Returns:
#   result - result of multiplication (int)

def GF_256_multiply(a, b, polynomial):

    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= polynomial
        b >>= 1

    return result

#-----------------------------------------------------------------------------------------------------------------------#

# Function that implements key dependant S-boxes and MDS:
#
# Takes as an input:
#   W - 32-bit word (binary in string)
#   ListOfWords - list of 32-bit words (binary in string) (list of strings)
# Returns:
#   Z - 32-bit word (binary in string)

def H_function(W, ListOfWords):

    MDS = [[1, 239, 91, 91],
           [91, 239, 239, 1],
           [239, 91, 1, 239],
           [239, 1, 239, 91]]

    if len(ListOfWords) == 4:
        x0 = int(W[24:32], 2)
        x1 = int(W[16:24], 2)
        x2 = int(W[8:16], 2)
        x3 = int(W[0:8], 2)

        x0 = q1(x0)
        x1 = q0(x1)
        x2 = q0(x2)
        x3 = q1(x3)

        x0 = bin(x0)[2:].zfill(8)
        x1 = bin(x1)[2:].zfill(8)
        x2 = bin(x2)[2:].zfill(8)
        x3 = bin(x3)[2:].zfill(8)

        W = x3 + x2 + x1 + x0

        W = int(W, 2) ^ int(ListOfWords[3], 2)

        W = bin(W)[2:].zfill(32)

    if len(ListOfWords) >= 3:
        x0 = int(W[24:32], 2)
        x1 = int(W[16:24], 2)
        x2 = int(W[8:16], 2)
        x3 = int(W[0:8], 2)

        x0 = q1(x0)
        x1 = q1(x1)
        x2 = q0(x2)
        x3 = q0(x3)

        x0 = bin(x0)[2:].zfill(8)
        x1 = bin(x1)[2:].zfill(8)
        x2 = bin(x2)[2:].zfill(8)
        x3 = bin(x3)[2:].zfill(8)

        W = x3 + x2 + x1 + x0

        W = int(W, 2) ^ int(ListOfWords[2], 2)

        W = bin(W)[2:].zfill(32)

    x0 = int(W[24:32], 2)
    x1 = int(W[16:24], 2)
    x2 = int(W[8:16], 2)
    x3 = int(W[0:8], 2)

    x0 = q0(x0)
    x1 = q1(x1)
    x2 = q0(x2)
    x3 = q1(x3)

    x0 = bin(x0)[2:].zfill(8)
    x1 = bin(x1)[2:].zfill(8)
    x2 = bin(x2)[2:].zfill(8)
    x3 = bin(x3)[2:].zfill(8)

    W = x3 + x2 + x1 + x0

    W = int(W, 2) ^ int(ListOfWords[1], 2)

    W = bin(W)[2:].zfill(32)

    x0 = int(W[24:32], 2)
    x1 = int(W[16:24], 2)
    x2 = int(W[8:16], 2)
    x3 = int(W[0:8], 2)

    x0 = q0(x0)
    x1 = q0(x1)
    x2 = q1(x2)
    x3 = q1(x3)

    x0 = bin(x0)[2:].zfill(8)
    x1 = bin(x1)[2:].zfill(8)
    x2 = bin(x2)[2:].zfill(8)
    x3 = bin(x3)[2:].zfill(8)

    W = x3 + x2 + x1 + x0

    W = int(W, 2) ^ int(ListOfWords[0], 2)

    W = bin(W)[2:].zfill(32)

    x0 = int(W[24:32], 2)
    x1 = int(W[16:24], 2)
    x2 = int(W[8:16], 2)
    x3 = int(W[0:8], 2)

    x0 = q1(x0)
    x1 = q0(x1)
    x2 = q1(x2)
    x3 = q0(x3)

    x0 = bin(x0)[2:].zfill(8)
    x1 = bin(x1)[2:].zfill(8)
    x2 = bin(x2)[2:].zfill(8)
    x3 = bin(x3)[2:].zfill(8)

    Word_vector = [[int(x0, 2)], [int(x1, 2)], [int(x2, 2)], [int(x3, 2)]]

    C = GF_256_multiply_Matrices(MDS, Word_vector, 0x169)

    Z = bin(C[3][0])[2:].zfill(8) + bin(C[2][0])[2:].zfill(8) + bin(C[1][0])[2:].zfill(8) + bin(C[0][0])[2:].zfill(8)

    return Z

#---------------------------------------------------------------------------#

# Function that generates subkeys K:
#
# Takes as an input:
#   Me - list of 32-bit words (binary in string) (list of strings)
#   Mo - list of 32-bit words (binary in string) (list of strings)
#   rounds - number of rounds (int) (16 by default)
# Returns:
#   K - list of 32-bit words (hex in string) (list of strings)

def generate_K(Me, Mo, rounds=16):
    rho = pow(2, 24) + pow(2, 16) + pow(2, 8) + pow(2, 0)

    K = []
    
    for i in range(rounds + 4):
        a = bin(2 * i * rho)[2:].zfill(32)
        A = int(H_function(a, Me), 2)
        b = bin(((2 * i) + 1) * rho)[2:].zfill(32)
        B = ROL(int(H_function(b, Mo), 2), 8, 32)
        K.append(hex((A + B) % pow(2, 32))[2:].zfill(8))
        K.append(hex(ROL(((A + (2 * B)) % pow(2, 32)), 9, 32))[2:].zfill(8))

    return K

#---------------------------------------------------------------------------#

# Function that returns value of H function, but with list of words = S:
#
# Note: 
#       g(X) = h(X, S) according to official TwoFish paper
#
# Takes as an input:
#   Word - 32-bit word (binary in string)
#   S - list of 32-bit words (binary in string) (list of strings)
# Returns:
#   H_function(Word, S) - 32-bit word (binary in string)

def g_function(Word, S):
    return H_function(Word, S)

#---------------------------------------------------------------------------#

# Function F (basis of each round):
#
# Takes as an input:
#   Word1 - 32-bit word (binary in string)
#   Word2 - 32-bit word (binary in string)
#   round - number of current round (int)
#   K - list of 32-bit subkeys K (binary in string) (list of strings)
#   S - list of 32-bit words (binary in string) (list of strings)
# Returns:
#   F0 - 32-bit word (binary in string)
#   F1 - 32-bit word (binary in string)

def F_function(Word1, Word2, round, K, S):
    T0 = g_function(Word1, S)
    T1 = g_function(bin(ROL(int(Word2, 2), 8, 32))[2:].zfill(32), S)
    F0 = ((int(T0, 2) + int(T1, 2) + int(K[2*round + 8], 16)) % (2**32))
    F1 = ((int(T0, 2) + 2*int(T1, 2) + int(K[2*round + 9], 16)) % (2**32))
    F0_bin = bin(F0)[2:].zfill(32)
    F1_bin = bin(F1)[2:].zfill(32)
    
    return F0_bin, F1_bin

#---------------------------------------------------------------------------#

# Function that formats ciphertext:
#
# Takes as an input:
#   ciphertext - 32-bit fragment of ciphertext (hex in string)
# Returns:
#   result - 32-bit fragment of formatted ciphertext (hex in string)

def format_CT(ciphertext):
    result = ciphertext[6:8] + ciphertext[4:6] + ciphertext[2:4] + ciphertext[0:2]
    return result

#---------------------------------------------------------------------------#

# Function that formats plaintext:
#
# Takes as an input:
#   text - string (hex in string)
# Returns:
#   PT - list of 128-bit fragments of formatted plaintext (hex in string) (list of strings)

def format_Plaintext(text):
    PT = []

    text_length_mod = len(text) % 32

    if(text_length_mod != 0):
        for i in range(32 - text_length_mod):
            text += "0"
    
    temp = ""
    for i in range(int(len(text)/8)):
        format_CT(text[8*i:8*(i+1)])
        temp += format_CT(text[8*i:8*(i+1)])

    for i in range(math.ceil(len(text)/32)):
        PT.append(temp[32*i:32*(i+1)])

    return PT

#---------------------------------------------------------------------------#

# Function that performs input whitening (in decryption):
#
# Takes as an input:
#   R0 - 1st 32-bit fragment of plaintext (int)
#   R1 - 2nd 32-bit fragment of plaintext (int)
#   R2 - 3rd 32-bit fragment of plaintext (int)
#   R3 - 4th 32-bit fragment of plaintext (int)
#   subkeys_K - list of 32-bit subkeys K (hex in string) (list of strings)
# Returns:
#   R0 - 1st 32-bit fragment of plaintext after input whitening (int)
#   R1 - 2nd 32-bit fragment of plaintext after input whitening (int)
#   R2 - 3rd 32-bit fragment of plaintext after input whitening (int)
#   R3 - 4th 32-bit fragment of plaintext after input whitening (int)

def input_whitening(R0, R1, R2, R3, subkeys_K):
    R0 = R0 ^ int(subkeys_K[0], 16)
    R1 = R1 ^ int(subkeys_K[1], 16)
    R2 = R2 ^ int(subkeys_K[2], 16)
    R3 = R3 ^ int(subkeys_K[3], 16)

    return R0, R1, R2, R3

#---------------------------------------------------------------------------#

# Function that performs input whitening (in encryption):
#
# Takes as an input:
#   formatted_plaintext - 128-bit fragment of formatted plaintext (hex in string)
#   subkeys_K - list of 32-bit subkeys K (hex in string) (list of strings)
# Returns:
#   R0 - 1st 32-bit fragment of plaintext after input whitening (int)
#   R1 - 2nd 32-bit fragment of plaintext after input whitening (int)
#   R2 - 3rd 32-bit fragment of plaintext after input whitening (int)
#   R3 - 4th 32-bit fragment of plaintext after input whitening (int)

def input_whitening2(formatted_plaintext, subkeys_K):
    R0 = int(formatted_plaintext[0:8], 16) ^ int(subkeys_K[0], 16)
    R1 = int(formatted_plaintext[8:16], 16) ^ int(subkeys_K[1], 16)
    R2 = int(formatted_plaintext[16:24], 16) ^ int(subkeys_K[2], 16)
    R3 = int(formatted_plaintext[24:32], 16) ^ int(subkeys_K[3], 16)

    return R0, R1, R2, R3

#---------------------------------------------------------------------------#

# Function that performs output whitening (in encryption):
#
# Takes as an input:
#   R0 - 1st 32-bit fragment of ciphertext (int)
#   R1 - 2nd 32-bit fragment of ciphertext (int)
#   R2 - 3rd 32-bit fragment of ciphertext (int)
#   R3 - 4th 32-bit fragment of ciphertext (int)
#   subkeys_K - list of 32-bit subkeys K (hex in string) (list of strings)
# Returns:
#   R0 - 1st 32-bit fragment of ciphertext after output whitening (int)
#   R1 - 2nd 32-bit fragment of ciphertext after output whitening (int)
#   R2 - 3rd 32-bit fragment of ciphertext after output whitening (int)
#   R3 - 4th 32-bit fragment of ciphertext after output whitening (int)

def output_whitening(R0, R1, R2, R3, subkeys_K):
    R0 = R0 ^ int(subkeys_K[4], 16)
    R1 = R1 ^ int(subkeys_K[5], 16)
    R2 = R2 ^ int(subkeys_K[6], 16)
    R3 = R3 ^ int(subkeys_K[7], 16)

    return R0, R1, R2, R3

#---------------------------------------------------------------------------#

# Function that performs output whitening (in encryption):
#
# Takes as an input:
#   formatted_plaintext - 128-bit fragment of formatted ciphertext (hex in string)
#   subkeys_K - list of 32-bit subkeys K (hex in string) (list of strings)
# Returns:
#   R0 - 1st 32-bit fragment of ciphertext after output whitening (int)
#   R1 - 2nd 32-bit fragment of ciphertext after output whitening (int)
#   R2 - 3rd 32-bit fragment of ciphertext after output whitening (int)
#   R3 - 4th 32-bit fragment of ciphertext after output whitening (int)

def output_whitening2(formatted_ciphertext, subkeys_K):
    R0 = int(formatted_ciphertext[0:8], 16) ^ int(subkeys_K[4], 16)
    R1 = int(formatted_ciphertext[8:16], 16) ^ int(subkeys_K[5], 16)
    R2 = int(formatted_ciphertext[16:24], 16) ^ int(subkeys_K[6], 16)
    R3 = int(formatted_ciphertext[24:32], 16) ^ int(subkeys_K[7], 16)

    return R0, R1, R2, R3

#---------------------------------------------------------------------------#

# Function that performs encryption:
#
# Takes as an input:
#   Plaintext - plaintext (hex in string)
#   Raw_Key - key that we want to use (hex in string)
#   mode - ECB or CBC (string)
# Returns:
#   result - ciphertext (hex in string)

def TwoFish_encrypt(Plaintext, Raw_Key, mode):
    try:
        int(Raw_Key, 16)  
    except ValueError:
        raise Exception("Please input only hexadecimal value as key.")
    try:
        int(Plaintext, 16)  
    except ValueError:
        raise Exception("Please input only hexadecimal value as plaintext.")

    if ((mode != 'ECB') and (mode != "CBC")):
        raise Exception("Choose ECB or CBC as mode")

    Key = format_Key(Raw_Key)
    PT = format_Plaintext(Plaintext)
    CT = []
    
    Me, Mo, S = key_Schedule(Key)
    K = generate_K(Me, Mo, 16)

    CT_i = "0"

    for plaintext in PT:
        if (mode == "CBC"):
            plaintext = hex(int(plaintext, 16) ^ int(CT_i, 16))[2:].zfill(32)
        R0, R1, R2, R3 = input_whitening2(plaintext, K)

        F0, F1 = F_function(bin(R0)[2:].zfill(32), bin(R1)[2:].zfill(32), 0, K, S)
        C2 = ROR(int(F0, 2) ^ R2, 1, 32)
        C3 = ROL(R3, 1, 32) ^ int(F1, 2)

        for i in range(15):
            R2 = R0
            R3 = R1
            R0 = C2
            R1 = C3

            F0, F1 = F_function(bin(R0)[2:].zfill(32), bin(R1)[2:].zfill(32), i + 1, K, S)
            C2 = ROR(int(F0, 2) ^ R2, 1, 32)
            C3 = ROL(R3, 1, 32) ^ int(F1, 2)

        R0, R1, R2, R3 = output_whitening(R0, R1, C2, C3, K)

        CT_i = format_CT(hex(R0)[2:].zfill(8)) + format_CT(hex(R1)[2:].zfill(8)) + format_CT(hex(R2)[2:].zfill(8)) + format_CT(hex(R3)[2:].zfill(8))
        CT.append(CT_i)

    result = ""
    for block in CT:
        result += block
    return result.upper()

#---------------------------------------------------------------------------#

# Function that performs decryption:
#
# Takes as an input:
#   Ciphertext - ciphertext (hex in string)
#   Raw_Key - key that we want to use (hex in string)
#   mode - ECB or CBC (string)
# Returns:
#   result - plaintext (hex in string)

def TwoFish_decrypt(Ciphertext, Raw_Key, mode):
    try:
        int(Raw_Key, 16)  
    except ValueError:
        raise Exception("Please input only hexadecimal value as key.")

    try:
        int(Ciphertext, 16)  
    except ValueError:
        raise Exception("Please input only hexadecimal value as cyphertext.")

    if ((mode != 'ECB') and (mode != "CBC")):
        raise Exception("Choose ECB or CBC as mode")

    Key = format_Key(Raw_Key)

    PT = []
    CT = format_Plaintext(Ciphertext)

    Me, Mo, S = key_Schedule(Key)
    K = generate_K(Me, Mo, 16)
    last_cipertext = "0"

    for ciphertext in CT:
        R0, R1, C2, C3 = output_whitening2(ciphertext, K)

        for i in range(15):
            F0, F1 = F_function(bin(R0)[2:].zfill(32), bin(R1)[2:].zfill(32), 15-i, K, S)
            R2 = ROL(C2, 1, 32) ^ int(F0, 2)
            R3 = ROR(C3^int(F1, 2), 1, 32)

            C2 = R0
            C3 = R1
            R0 = R2
            R1 = R3
        
        F0, F1 = F_function(bin(R0)[2:].zfill(32), bin(R1)[2:].zfill(32), 0, K, S)
        R2 = ROL(C2, 1, 32) ^ int(F0, 2)
        R3 = ROR(C3^int(F1, 2), 1, 32)

        R0, R1, R2, R3 = input_whitening(R0, R1, R2, R3, K)

        Pt_i = format_CT(hex(R0)[2:].zfill(8)) + format_CT(hex(R1)[2:].zfill(8)) + format_CT(hex(R2)[2:].zfill(8)) + format_CT(hex(R3)[2:].zfill(8))

        if (mode == "CBC"):
            Pt_i = hex(int(Pt_i, 16) ^ int(last_cipertext, 16))[2:].zfill(32)

        PT.append(Pt_i)    
        last_cipertext = ciphertext  



    result = ""
    for block in PT:
        result += block
    return result.upper()

#---------------------------------------------------------------------------#

def main():
    key = (input("Input key in hexadecimal: "))
    plain = (input("Input plaintext in hexadecimal: "))
    mode = (input("Input mode: ")).strip()

    print("Ciphertext: ", TwoFish_encrypt(plain, key, mode))
    print("Decoded plaintext: ", TwoFish_decrypt(TwoFish_encrypt(plain, key, mode), key, mode))

if __name__ == "__main__":
    main()
