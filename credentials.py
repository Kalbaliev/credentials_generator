import yaml
from cryptography.fernet import Fernet
import os

class Credentials:
    """
    Credentials class for managing keys and credentials.

    Methods:
    - security_key_generator(system_name, security_keys=None): Create a new security key.
    - load_security_keys(): Load existing security keys from a YAML file.
    - update_security_key(system_name): Update the security keys by generating a new key for the specified system_name.
    - encrypt_decryptor(text, security_key, encrypt=True): Encrypt or decrypt text using a security key.
    - load_credentials(): Load existing encrypted credentials from a YAML file.
    - credentials_encrypt_decryptor(security_key, credentials, encrypt=True, encrypted_credentials=None):
        Encrypt or decrypt credentials using a security key.
    """

    @staticmethod
    def security_key_generator(system_name, security_keys=None):
        """
        Generate a new security key for the specified API_NAME.
        If security_keys is provided, update it with the new key.
        Store the security keys in a YAML file.

        Args:
            system_name (str): Name of the System.
            security_keys (dict): Existing security keys.

        Returns:
            dict: Updated security keys.
        """
        if security_keys is None:
            security_keys = {}

        security_key = Fernet.generate_key()
        security_keys[system_name] = security_key

        with open('security_keys.yaml', 'w') as security_keys_file:
            yaml.dump(security_keys, security_keys_file)

        return security_keys

    @staticmethod
    def load_security_keys():
        """
        Load the existing security keys from a YAML file.

        Returns:
            dict or None: Loaded security keys or None if the file is not found.
        """
        if os.path.exists('security_keys.yaml'):
            with open('security_keys.yaml', 'r') as security_keys_file:
                security_keys = yaml.safe_load(security_keys_file) or {}
            return security_keys
        else:
            print('security_keys.yaml file not found')
            return None

    def update_security_key(self, system_name):
        """
        Update the security keys by generating a new key for the specified API_NAME.

        Args:
            system_name (str): Name of the System.

        Returns:
            dict or None: Updated security keys or None if the file is not found.
        """
        security_keys = self.load_security_keys()
        security_keys = self.security_key_generator(system_name, security_keys)
        return security_keys

    @staticmethod
    def encrypt_decryptor(text, security_key, encrypt=True):
        """
        Encrypt or decrypt text using a security key.

        Args:
            text (str): Text to be encrypted or decrypted.
            security_key (str): Security key for encryption or decryption.
            encrypt (bool): True for encryption, False for decryption.

        Returns:
            str: Encrypted or decrypted text.
        """
        fernet = Fernet(security_key)

        if encrypt:
            encoded_text = text.encode()
            full_text = fernet.encrypt(encoded_text)
        else:
            decoded_text = fernet.decrypt(text)
            full_text = decoded_text.decode()

        return full_text

    @staticmethod
    def load_credentials():
        """
        Load the existing encrypted credentials from a YAML file.

        Returns:
            dict or None: Loaded encrypted credentials or None if the file is not found.
        """
        if os.path.exists('credentials.yaml'):
            with open('credentials.yaml', 'r') as credentials_file:
                encrypted_credentials = yaml.safe_load(credentials_file) or {}
            return encrypted_credentials
        else:
            print('credentials.yaml file not found')
            return None

    @classmethod
    def credentials_encrypt_decryptor(cls, security_key, credentials, encrypt=True, encrypted_credentials=None):
        """
        Encrypt or decrypt credentials using a security key.
        If encrypted_credentials is provided, update it with the encrypted/decrypted credentials.
        Store the encrypted credentials in a YAML file.

        Args:
            security_key (str): Security key for encryption or decryption.
            credentials (dict): Credentials to be encrypted or decrypted.
            encrypt (bool): True for encryption, False for decryption.
            encrypted_credentials (dict): Existing encrypted credentials.

        Returns:
            dict: Updated encrypted credentials.
        """
        if encrypt:
            if encrypted_credentials is None:
                encrypted_credentials = {}

            encrypted_credentials = {
                key: cls.encrypt_decryptor(value, security_key, encrypt)
                for key, value in credentials.items()
            }

            with open('credentials.yaml', 'w') as credentials_file:
                yaml.dump(encrypted_credentials, credentials_file)

            return encrypted_credentials
        else:
            if os.path.exists('credentials.yaml'):
                with open('credentials.yaml', 'r') as credentials_file:
                    encrypted_credentials = yaml.safe_load(credentials_file)
            else:
                print('credentials.yaml file not found')
                return None

            decrypted_credentials = {
                key: cls.encrypt_decryptor(value, security_key, encrypt)
                for key, value in encrypted_credentials.items()
            }

            return decrypted_credentials
