# Vigenère Cipher

## Information
The Vigenère Cipher is a poly-alphabetic substitution cipher first described by Giovan Battista Bellaso in 1553. This cipher is easy to understand and implement but is quite hard to crack. It resisted all attempts to break for three centuries which earned it the description "the indecipherable cipher".

In the 19th century the scheme was misattributed to <a href="https://en.wikipedia.org/wiki/Blaise_de_Vigen%C3%A8re">Blaise de Vigenère</a>, and so acquired its present name.

For more information about this cipher <a href="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher">click here</a>.

# Usage
## Encryption

To encrypt a message, use the encrypt() function that takes in two arguments: the plaintext (a string) and the keyword (also a string) and outputs the ciphertext.

Example (Identical input & output in both cases):
```
>>> encrypt("Hello World", "lorem ipsum")
Ttdqb Fekgq
```

## Decryption

To decrypt a message, use the decrypt() function that likewise takes in two similar arguments: the ciphertext and the keyword and outputs the plaintext.

Example (Identical input & output in both cases):
```
>>> decrypt("Ttdqb Fekgq", "lorem ipsum")
Hello World
```

# Committing
Pull requests are welcome.
