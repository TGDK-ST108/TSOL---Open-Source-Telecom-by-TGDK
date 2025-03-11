# ============================================================================
#                     TGDK OPEN SOURCE LICENSE (TSOL)
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
#   - Commercial use/distribution prohibited without explicit consent.
#   - Unauthorized modification or duplication of TichenorCode security
#     modules strictly prohibited.
#
# Licensed under TSOL/BFE Licensing.
# Full License and Security Details: https://olivia-tgdk.com/license
# ============================================================================

import hashlib
import json

class PacketValidator:
    def __init__(self, t_code_key):
        self.t_code_key = t_code_key

    def sign_packet(self, packet_data):
        packet_json = json.dumps(packet_data, sort_keys=True)
        signature = hashlib.sha384((packet_json + self.t_code_key).encode()).hexdigest()
        packet_data['signature'] = signature
        return packet_data

    def verify_packet(self, packet_data):
        signature = packet_data.pop('signature', None)
        expected_signature = self.sign_packet(packet_data)['signature']
        return hashlib.compare_digest(signature, expected_signature)

# Example usage:
# validator = PacketValidator(t_code_key="securekey123")
# packet = {"user":"Sean","action":"authenticate"}
# signed_packet = validator.sign_packet(packet)
# validator.verify_packet(signed_packet)