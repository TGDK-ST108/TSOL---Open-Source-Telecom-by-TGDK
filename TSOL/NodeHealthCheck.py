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

import requests
import hashlib

class NodeHealthCheck:
    def __init__(self, node_endpoint, t_code_key):
        self.node_endpoint = node_endpoint
        self.t_code_key = t_code_key

    def check_status(self):
        response = requests.get(self.node_endpoint)
        status_data = response.json()
        integrity_hash = self._hash_status(status_data)
        return {'status_data': status_data, 'integrity_hash': integrity_hash}

    def _hash_status(self, data):
        data_str = str(sorted(data.items()))
        combined = f"{data_str}:{self.t_code_key}"
        return hashlib.sha384(combined.encode()).hexdigest()

# Example Usage:
# health_check = NodeHealthCheck("https://api.tgdktelecom.com/node_status", "securekey123")
# status = health_check.check_status()
