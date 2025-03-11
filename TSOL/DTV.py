# ============================================================================
#                   TGDK OPEN SOURCE LICENSE (TSOL)
#                GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
#
# © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.
#
# Security Framework: TichenorCode (T-Code)
# Developed exclusively by Sean Tichenor for TGDK.
#
# Permissions:
#   - Non-commercial use, modification, redistribution allowed.
#   - Mandatory attribution on all derivatives.
#
# Restrictions:
#   - Commercial use prohibited without explicit authorization.
#   - Unauthorized use of TichenorCode modules prohibited.
#
# Licensed under TSOL/BFE Licensing.
# https://olivia-tgdk.com/license
# ============================================================================

import hashlib
import json

class DataTransferValidator:
    def __init__(self, t_code_key):
        self.t_code_key = t_code_key

    def encode_transfer(self, payload):
        serialized_payload = json.dumps(payload, sort_keys=True)
        integrity_token = self._generate_hash(serialized_payload)
        return {'payload': payload, 'integrity_token': integrity_token}

    def validate_transfer(self, received_payload, received_token):
        serialized_payload = json.dumps(received_payload, sort_keys=True)
        expected_token = self._generate_hash(serialized_payload)
        return hashlib.compare_digest(received_token, expected_token)

    def _generate_hash(self, serialized_payload):
        combined = f"{serialized_payload}:{self.t_code_key}"
        return hashlib.sha512(combined.encode()).hexdigest()

# Example Usage:
# validator = DataTransferValidator(t_code_key="securekey123")
# transfer = validator.encode_transfer({"data": "secure information"})