# Twofish Python Implementation

This project implements the Twofish symmetric key block cipher in Python. Twofish is a symmetric key block cipher with a block size of 128 bits and key sizes up to 256 bits. The cipher was designed by Bruce Schneier, John Kelsey, Doug Whiting, David Wagner, Chris Hall, and Niels Ferguson and was one of the five finalists of the Advanced Encryption Standard (AES) contest, but it was not selected for standardization.

## Implementation Details

While implementing functions for this project we strictly followed the steps from the official paper titled: [Twofish: A 128-Bit Block Cipher](https://www.researchgate.net/publication/245272403_Twofish_A_128Bit_Block_Cipher). Our implementation supports both ECB (Electronic Codebook) and CBC (Cipher Block Chaining) modes of operation.


## Usage

To use this implementation in your Python projects, simply import the necessary functions from the provided modules. Ensure that you have Python installed on your system.

Clone the repo:
```console
git clone https://github.com/K-Czaplicki/TwoFish.git
```



Example usage:

```python
import sys
sys.path.append('/path/to/TwoFish')
from TwoFish import *

key = text_To_Hex("This is a key")
plain = text_To_Hex("This is an example")
mode = "ECB"

# Encrypt
ciphertext = TwoFish_encrypt(plain, key, mode)

# Decrypt
decoded_plaintext = hex_To_Text(TwoFish_decrypt(ciphertext, key, mode))

print("Ciphertext: ", ciphertext)
print("Decoded plaintext:", decoded_plaintext)
```

The result of running this example should be:
```console
Ciphertext:  533FC35A0030003689E7D1D9F2E6781A6F5555EFC8AB9531A103EC74E406C969
Decoded plaintext: This is an example
```


## Testing

The implementation has been thoroughly tested using test vectors provided by the official paper. Test vectors are sets of known inputs and their corresponding outputs, used to verify the correctness of the implementation.


## Authors

- [@K-Czaplicki](https://github.com/K-Czaplicki)
- [@morzelowski](https://github.com/morzelowski)
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
