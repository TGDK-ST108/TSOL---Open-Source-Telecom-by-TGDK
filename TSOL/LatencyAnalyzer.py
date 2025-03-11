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

import subprocess
import hashlib

class LatencyAnalyzer:
    def __init__(self, target_host, t_code_key):
        self.target_host = target_host
        self.t_code_key = t_code_key

    def measure_latency(self):
        response = subprocess.run(
            ["ping", "-c", "4", self.target_host],
            capture_output=True, text=True
        )
        latency_data = response.stdout
        integrity_hash = self._generate_hash(latency_data)
        return {'latency_data': latency_data, 'integrity_hash': integrity_hash}

    def _generate_hash(self, data):
        combined = f"{data}:{self.t_code_key}"
        return hashlib.sha512(combined.encode()).hexdigest()

# Example Usage:
# analyzer = LatencyAnalyzer("olivia-tgdk.com", t_code_key="securekey123")
# latency = analyzer.measure_latency()
