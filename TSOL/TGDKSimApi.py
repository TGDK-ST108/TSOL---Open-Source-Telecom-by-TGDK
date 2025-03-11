# ============================================================================
#                    TGDK OPEN SOURCE LICENSE (TSOL)
#                  GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
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
#   - Strictly prohibited: Commercial use or distribution without explicit
#     written consent from TGDK and Sean Tichenor.
#   - Unauthorized duplication or modification of TichenorCode (T-Code)
#     security modules is strictly prohibited.
#
# Original Work © 2025 TGDK & Sean Tichenor.
# Licensed under TSOL/BFE Licensing.
#
# Full License and Security Details: https://olivia-tgdk.com/license
# ============================================================================

import hashlib
import base64
from datetime import datetime

class TGDK_SIM_API:
    def __init__(self, sim_id, t_code_key):
        self.sim_id = sim_id
        self.t_code_key = t_code_key

    def generate_auth_token(self):
        timestamp = datetime.utcnow().isoformat()
        raw_token = f"{self.sim_id}:{timestamp}:{self.t_code_key}"
        sha_signature = hashlib.sha512(raw_token.encode()).digest()
        return base64.urlsafe_b64encode(sha_signature).decode()

    def verify_auth_token(self, token, timestamp, tolerance_seconds=60):
        expected_token = self.generate_auth_token_for_timestamp(timestamp)
        token_time = datetime.fromisoformat(timestamp)
        current_time = datetime.utcnow()
        if (current_time - token_time).seconds > tolerance_seconds:
            return False
        return hashlib.compare_digest(expected_token, token)

    def generate_auth_token_for_timestamp(self, timestamp):
        raw_token = f"{self.sim_id}:{timestamp}:{self.t_code_key}"
        sha_signature = hashlib.sha512(raw_token.encode()).digest()
        return base64.urlsafe_b64encode(sha_signature).decode()

# Example usage:
# sim_api = TGDK_SIM_API(sim_id="TGDKSIM-01", t_code_key="securekey123")
# token = sim_api.generate_auth_token()