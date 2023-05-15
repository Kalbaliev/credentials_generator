# Credentials Generator
Repository is designed to manage keys and credentials. It provides functionality to generate and update security keys, encrypt and decrypt text using a security key, and load and manipulate encrypted credentials stored in a YAML file. These methods facilitate secure handling of sensitive information in applications.


## Methods

- `security_key_generator(system_name, security_keys=None)`: Create a new security key.
- `load_security_keys()`: Load existing security keys from a YAML file.
- `update_security_key(system_name)`: Update the security keys by generating a new key for the specified system_name.
- `encrypt_decryptor(text, security_key, encrypt=True)`: Encrypt or decrypt text using a security key.
- `load_credentials()`: Load existing encrypted credentials from a YAML file.
- `credentials_encrypt_decryptor(security_key, credentials, encrypt=True, encrypted_credentials=None)`: Encrypt or decrypt credentials using a security key.

## Usage

Instantiate the `Credentials` class and use its methods to manage keys and credentials.

```python
from credentials import Credentials

# Create a new security key
security_keys = Credentials.security_key_generator("System_name")

# Load existing security keys
existing_keys = Credentials.load_security_keys()

# Update security keys
updated_keys = Credentials().update_security_key("System_name")

# Encrypt text
encrypted_text = Credentials.encrypt_decryptor("my_secret_text", security_key)

# Decrypt text
decrypted_text = Credentials.encrypt_decryptor(encrypted_text, security_key, encrypt=False)

# Load existing encrypted credentials
encrypted_credentials = Credentials.load_credentials()

# Encrypt credentials
encrypted = Credentials.credentials_encrypt_decryptor(security_key, credentials)

# Decrypt credentials
decrypted = Credentials.credentials_encrypt_decryptor(security_key, encrypted, encrypt=False)
