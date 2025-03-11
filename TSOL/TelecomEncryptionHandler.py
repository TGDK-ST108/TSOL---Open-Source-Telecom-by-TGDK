# ============================================================================
#                     TGDK OPEN SOURCE LICENSE (TSOL)
#                  GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
#
# © 2025 Sean Tichenor, TGDK & OliviaAI. All Rights Reserved.
#
# Security Framework: TichenorCode (T-Code)
# Exclusively developed by Sean Tichenor for TGDK.
#
# Permissions: Non-commercial use allowed. Attribution required.
# Restrictions: Unauthorized commercial use or modification prohibited.
#
# Licensed under TSOL/BFE Licensing.
# https://olivia-tgdk.com/license
# ============================================================================

from cryptography.fernet import Fernet
import hashlib

class TelecomEncryptionHandler:
    def __init__(self, t_code_key):
        self.t_code_key = t_code_key
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        encrypted = self.cipher.encrypt(data.encode())
        integrity_hash = hashlib.sha512(encrypted + self.t_code_key.encode()).hexdigest()
        return {'encrypted_data': encrypted, 'integrity_hash': integrity_hash}

    def decrypt_data(self, encrypted_data, integrity_hash):
        if hashlib.sha512(encrypted_data + self.t_code_key.encode()).hexdigest() != integrity_hash:
            raise ValueError("Data integrity check failed.")
        return self.cipher.decrypt(encrypted_data).decode()

# Example Usage:
# handler = TelecomEncryptionHandler(t_code_key="securekey123")
# encrypted = handler.encrypt_data("Sensitive Telecom Data")
