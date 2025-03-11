# ============================================================================
#                    TGDK OPEN SOURCE LICENSE (TSOL)
#                 GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
#
# © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.
#
# Security Framework: TichenorCode (T-Code)
# Developed by Sean Tichenor exclusively for TGDK.
#
# Permissions:
#   - Non-commercial use, modification, redistribution permitted.
#   - Attribution mandatory on all derivative works.
#
# Restrictions:
#   - Commercial use or distribution prohibited without explicit consent.
#   - Unauthorized duplication/modification of TichenorCode security modules
#     is strictly prohibited.
#
# Licensed under TSOL/BFE Licensing.
# Full License and Security Details: https://olivia-tgdk.com/license
# ============================================================================

import hashlib

class TGDK_DataIntegrity:
    def __init__(self, t_code_key):
        self.t_code_key = t_code_key

    def generate_integrity_hash(self, data):
        data_encoded = data.encode('utf-8')
        hash_object = hashlib.sha256(data_encoded + self.t_code_key.encode())
        return hash_object.hexdigest()

    def verify_integrity(self, data, provided_hash):
        calculated_hash = self.generate_integrity_hash(data)
        return hashlib.compare_digest(calculated_hash, provided_hash)

# Example usage:
# integrity = TGDK_DataIntegrity(t_code_key="securekey123")
# data_hash = integrity.generate_integrity_hash("Sensitive data")
# integrity.verify_integrity("Sensitive data", data_hash)