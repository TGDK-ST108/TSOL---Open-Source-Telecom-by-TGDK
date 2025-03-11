# ============================================================================
#                       TGDK OPEN SOURCE LICENSE (TSOL)
#                    GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
#
# © 2025 Sean Tichenor, TGDK & OliviaAI. All Rights Reserved.
#
# Security Framework: TichenorCode (T-Code)
# Exclusively developed by Sean Tichenor for TGDK.
#
# Permissions: Non-commercial use, modification, redistribution allowed.
# Attribution required.
#
# Restrictions:
#   - Commercial use prohibited without explicit authorization.
#   - Unauthorized duplication or modification of TichenorCode prohibited.
#
# Licensed under TSOL/BFE Licensing.
# Full details at: https://olivia-tgdk.com/license
# ============================================================================

import hashlib

class TelecomFirewall:
    def __init__(self, allowed_ips, t_code_key):
        self.allowed_ips = allowed_ips
        self.t_code_key = t_code_key

    def verify_ip(self, incoming_ip):
        hashed_ip = hashlib.sha384(f"{incoming_ip}:{self.t_code_key}".encode()).hexdigest()
        allowed_hashes = [hashlib.sha384(f"{ip}:{self.t_code_key}".encode()).hexdigest() for ip in self.allowed_ips]
        return hashed_ip in allowed_hashes

# Example Usage:
# firewall = TelecomFirewall(["192.168.1.10", "10.0.0.5"], t_code_key="securekey123")
# firewall.verify_ip("192.168.1.10")