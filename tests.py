############### TwoFish tests ###############

import unittest

from TwoFish import TwoFish_encrypt
from TwoFish import TwoFish_decrypt

class Encryption_Testing(unittest.TestCase): 
    
    def test_encryption_1(self):
        key1 = "00000000000000000000000000000000"
        plaintext1 = "00000000000000000000000000000000"
        ciphertext1 = "9F589F5CF6122C32B6BFEC2F2AE8C35A"
        self.assertEqual(ciphertext1, TwoFish_encrypt(plaintext1, key1, "ECB"))

    def test_encryption_2(self):
        key2 = "00000000000000000000000000000000"
        plaintext2 = "9F589F5CF6122C32B6BFEC2F2AE8C35A"
        ciphertext2 = "D491DB16E7B1C39E86CB086B789F5419"
        self.assertEqual(ciphertext2, TwoFish_encrypt(plaintext2, key2, "ECB"))

    def test_encryption_3(self):
        key3 = "9F589F5CF6122C32B6BFEC2F2AE8C35A"
        plaintext3 = "D491DB16E7B1C39E86CB086B789F5419"
        ciphertext3 = "019F9809DE1711858FAAC3A3BA20FBC3"
        self.assertEqual(ciphertext3, TwoFish_encrypt(plaintext3, key3, "ECB"))

    def test_encryption_4(self):
        key4 = "D491DB16E7B1C39E86CB086B789F5419"
        plaintext4 = "019F9809DE1711858FAAC3A3BA20FBC3"
        ciphertext4 = "6363977DE839486297E661C6C9D668EB"
        self.assertEqual(ciphertext4, TwoFish_encrypt(plaintext4, key4, "ECB"))
    
    def test_encryption_5(self):
        key5 = "019F9809DE1711858FAAC3A3BA20FBC3"
        plaintext5 = "6363977DE839486297E661C6C9D668EB"
        ciphertext5 = "816D5BD0FAE35342BF2A7412C246F752"
        self.assertEqual(ciphertext5, TwoFish_encrypt(plaintext5, key5, "ECB"))

    def test_encryption_6(self):
        key6 = "000000000000000000000000000000000000000000000000"
        plaintext6 = "00000000000000000000000000000000"
        ciphertext6 = "EFA71F788965BD4453F860178FC19101"
        self.assertEqual(ciphertext6, TwoFish_encrypt(plaintext6, key6, "ECB"))
    
    def test_encryption_7(self):
        key7 = "000000000000000000000000000000000000000000000000"
        plaintext7 = "EFA71F788965BD4453F860178FC19101"
        ciphertext7 = "88B2B2706B105E36B446BB6D731A1E88"
        self.assertEqual(ciphertext7, TwoFish_encrypt(plaintext7, key7, "ECB"))

    def test_encryption_8(self):
        key8 = "EFA71F788965BD4453F860178FC191010000000000000000"
        plaintext8 = "88B2B2706B105E36B446BB6D731A1E88"
        ciphertext8 = "39DA69D6BA4997D585B6DC073CA341B2"
        self.assertEqual(ciphertext8, TwoFish_encrypt(plaintext8, key8, "ECB"))

    def test_encryption_9(self):
        key9 = "88B2B2706B105E36B446BB6D731A1E88EFA71F788965BD44"
        plaintext9 = "39DA69D6BA4997D585B6DC073CA341B2"
        ciphertext9 = "182B02D81497EA45F9DAACDC29193A65"
        self.assertEqual(ciphertext9, TwoFish_encrypt(plaintext9, key9, "ECB"))
    
    def test_encryption_10(self):
        key10 = "39DA69D6BA4997D585B6DC073CA341B288B2B2706B105E36"
        plaintext10 = "182B02D81497EA45F9DAACDC29193A65"
        ciphertext10 = "7AFF7A70CA2FF28AC31DD8AE5DAAAB63"
        self.assertEqual(ciphertext10, TwoFish_encrypt(plaintext10, key10, "ECB"))

    def test_encryption_11(self):
        key11 = "0000000000000000000000000000000000000000000000000000000000000000"
        plaintext11 = "00000000000000000000000000000000"
        ciphertext11 = "57FF739D4DC92C1BD7FC01700CC8216F"
        self.assertEqual(ciphertext11, TwoFish_encrypt(plaintext11, key11, "ECB"))

    def test_encryption_12(self):
        key12 = "0000000000000000000000000000000000000000000000000000000000000000"
        plaintext12 = "57FF739D4DC92C1BD7FC01700CC8216F"
        ciphertext12 = "D43BB7556EA32E46F2A282B7D45B4E0D"
        self.assertEqual(ciphertext12, TwoFish_encrypt(plaintext12, key12, "ECB"))

    def test_encryption_13(self):
        key13 = "57FF739D4DC92C1BD7FC01700CC8216F00000000000000000000000000000000"
        plaintext13 = "D43BB7556EA32E46F2A282B7D45B4E0D"
        ciphertext13 = "90AFE91BB288544F2C32DC239B2635E6"
        self.assertEqual(ciphertext13, TwoFish_encrypt(plaintext13, key13, "ECB"))

    def test_encryption_14(self):
        key14 = "D43BB7556EA32E46F2A282B7D45B4E0D57FF739D4DC92C1BD7FC01700CC8216F"
        plaintext14 = "90AFE91BB288544F2C32DC239B2635E6"
        ciphertext14 = "6CB4561C40BF0A9705931CB6D408E7FA"
        self.assertEqual(ciphertext14, TwoFish_encrypt(plaintext14, key14, "ECB"))

    def test_encryption_15(self):
        key15 = "90AFE91BB288544F2C32DC239B2635E6D43BB7556EA32E46F2A282B7D45B4E0D"
        plaintext15 = "6CB4561C40BF0A9705931CB6D408E7FA"
        ciphertext15 = "3059D6D61753B958D92F4781C8640E58"
        self.assertEqual(ciphertext15, TwoFish_encrypt(plaintext15, key15, "ECB"))


class Decryption_Testing(unittest.TestCase):
    def test_decryption_1(self):
        key1 = "00000000000000000000000000000000"
        plaintext1 = "00000000000000000000000000000000"
        ciphertext1 = "9F589F5CF6122C32B6BFEC2F2AE8C35A"
        self.assertEqual(plaintext1, TwoFish_decrypt(ciphertext1, key1, "ECB"))

    def test_decryption_2(self):
        key2 = "00000000000000000000000000000000"
        plaintext2 = "9F589F5CF6122C32B6BFEC2F2AE8C35A"
        ciphertext2 = "D491DB16E7B1C39E86CB086B789F5419"
        self.assertEqual(plaintext2, TwoFish_decrypt(ciphertext2, key2, "ECB"))

    def test_decryption_3(self):
        key3 = "9F589F5CF6122C32B6BFEC2F2AE8C35A"
        plaintext3 = "D491DB16E7B1C39E86CB086B789F5419"
        ciphertext3 = "019F9809DE1711858FAAC3A3BA20FBC3"
        self.assertEqual(plaintext3, TwoFish_decrypt(ciphertext3, key3, "ECB"))

    def test_decryption_4(self):
        key4 = "D491DB16E7B1C39E86CB086B789F5419"
        plaintext4 = "019F9809DE1711858FAAC3A3BA20FBC3"
        ciphertext4 = "6363977DE839486297E661C6C9D668EB"
        self.assertEqual(plaintext4, TwoFish_decrypt(ciphertext4, key4, "ECB"))
    
    def test_decryption_5(self):
        key5 = "019F9809DE1711858FAAC3A3BA20FBC3"
        plaintext5 = "6363977DE839486297E661C6C9D668EB"
        ciphertext5 = "816D5BD0FAE35342BF2A7412C246F752"
        self.assertEqual(plaintext5, TwoFish_decrypt(ciphertext5, key5, "ECB"))

    def test_decryption_6(self):
        key6 = "000000000000000000000000000000000000000000000000"
        plaintext6 = "00000000000000000000000000000000"
        ciphertext6 = "EFA71F788965BD4453F860178FC19101"
        self.assertEqual(plaintext6, TwoFish_decrypt(ciphertext6, key6, "ECB"))
    
    def test_decryption_7(self):
        key7 = "000000000000000000000000000000000000000000000000"
        plaintext7 = "EFA71F788965BD4453F860178FC19101"
        ciphertext7 = "88B2B2706B105E36B446BB6D731A1E88"
        self.assertEqual(plaintext7, TwoFish_decrypt(ciphertext7, key7, "ECB"))

    def test_decryption_8(self):
        key8 = "EFA71F788965BD4453F860178FC191010000000000000000"
        plaintext8 = "88B2B2706B105E36B446BB6D731A1E88"
        ciphertext8 = "39DA69D6BA4997D585B6DC073CA341B2"
        self.assertEqual(plaintext8, TwoFish_decrypt(ciphertext8, key8, "ECB"))

    def test_decryption_9(self):
        key9 = "88B2B2706B105E36B446BB6D731A1E88EFA71F788965BD44"
        plaintext9 = "39DA69D6BA4997D585B6DC073CA341B2"
        ciphertext9 = "182B02D81497EA45F9DAACDC29193A65"
        self.assertEqual(plaintext9, TwoFish_decrypt(ciphertext9, key9, "ECB"))
    
    def test_decryption_10(self):
        key10 = "39DA69D6BA4997D585B6DC073CA341B288B2B2706B105E36"
        plaintext10 = "182B02D81497EA45F9DAACDC29193A65"
        ciphertext10 = "7AFF7A70CA2FF28AC31DD8AE5DAAAB63"
        self.assertEqual(plaintext10, TwoFish_decrypt(ciphertext10, key10, "ECB"))

    def test_decryption_11(self):
        key11 = "0000000000000000000000000000000000000000000000000000000000000000"
        plaintext11 = "00000000000000000000000000000000"
        ciphertext11 = "57FF739D4DC92C1BD7FC01700CC8216F"
        self.assertEqual(plaintext11, TwoFish_decrypt(ciphertext11, key11, "ECB"))

    def test_decryption_12(self):
        key12 = "0000000000000000000000000000000000000000000000000000000000000000"
        plaintext12 = "57FF739D4DC92C1BD7FC01700CC8216F"
        ciphertext12 = "D43BB7556EA32E46F2A282B7D45B4E0D"
        self.assertEqual(plaintext12, TwoFish_decrypt(ciphertext12, key12, "ECB"))

    def test_decryption_13(self):
        key13 = "57FF739D4DC92C1BD7FC01700CC8216F00000000000000000000000000000000"
        plaintext13 = "D43BB7556EA32E46F2A282B7D45B4E0D"
        ciphertext13 = "90AFE91BB288544F2C32DC239B2635E6"
        self.assertEqual(plaintext13, TwoFish_decrypt(ciphertext13, key13, "ECB"))

    def test_decryption_14(self):
        key14 = "D43BB7556EA32E46F2A282B7D45B4E0D57FF739D4DC92C1BD7FC01700CC8216F"
        plaintext14 = "90AFE91BB288544F2C32DC239B2635E6"
        ciphertext14 = "6CB4561C40BF0A9705931CB6D408E7FA"
        self.assertEqual(plaintext14, TwoFish_decrypt(ciphertext14, key14, "ECB"))

    def test_decryption_15(self):
        key15 = "90AFE91BB288544F2C32DC239B2635E6D43BB7556EA32E46F2A282B7D45B4E0D"
        plaintext15 = "6CB4561C40BF0A9705931CB6D408E7FA"
        ciphertext15 = "3059D6D61753B958D92F4781C8640E58"
        self.assertEqual(plaintext15, TwoFish_decrypt(ciphertext15, key15, "ECB"))
    
class Big_Test_encryption_128bit(unittest.TestCase):
    def test_encryption(self):
        key1 = "00000000000000000000000000000000"
        plaintext1 = "00000000000000000000000000000000"
        ciphertext1 = "5D9D4EEFFA9151575524F115815A12E0"
        for i in range(49):
            temp = TwoFish_encrypt(plaintext1, key1, "ECB")
            key1 = plaintext1
            plaintext1 = temp

        self.assertEqual(ciphertext1, temp)

if __name__ == '__main__':
    unittest.main()
