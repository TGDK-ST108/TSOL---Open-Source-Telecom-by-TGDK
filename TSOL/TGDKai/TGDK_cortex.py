# ============================================================================
#                       TGDK OPEN SOURCE LICENSE (TSOL)
#                    GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
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

import hashlib
import json

class TGDK_Cortex:
    def __init__(self, cortex_data, t_code_key):
        self.cortex_data = cortex_data
        self.t_code_key = t_code_key

    def encode_data(self):
        payload = json.dumps(self.cortex_data, sort_keys=True)
        encoded_hash = hashlib.sha384((payload + self.t_code_key).encode()).hexdigest()
        return {'payload': self.cortex_data, 'auth_hash': encoded_hash}

    def verify_data(self, received_payload, auth_hash):
        expected = hashlib.sha384((json.dumps(received_payload, sort_keys=True) + self.t_code_key).encode()).hexdigest()
        return hashlib.compare_digest(expected, auth_hash)

# Example Usage:
# cortex = TGDK_Cortex(cortex_data={"status": "active"}, t_code_key="securekey123")
# secured_data = cortex.encode_data()