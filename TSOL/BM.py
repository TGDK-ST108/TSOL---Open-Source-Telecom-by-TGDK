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
#   - Unauthorized duplication or modification of TichenorCode prohibited.
#
# Licensed under TSOL/BFE Licensing.
# https://olivia-tgdk.com/license
# ============================================================================

import psutil
import hashlib

class BandwidthMonitor:
    def __init__(self, interface, t_code_key):
        self.interface = interface
        self.t_code_key = t_code_key

    def get_bandwidth_usage(self):
        counters = psutil.net_io_counters(pernic=True)[self.interface]
        data = {'bytes_sent': counters.bytes_sent, 'bytes_recv': counters.bytes_recv}
        data['integrity_hash'] = self._generate_integrity_hash(data)
        return data

    def _generate_integrity_hash(self, data):
        payload = f"{data['bytes_sent']}:{data['bytes_recv']}:{self.t_code_key}"
        return hashlib.sha256(payload.encode()).hexdigest()

# Example Usage:
# monitor = BandwidthMonitor(interface="eth0", t_code_key="securekey123")
# usage = monitor.get_bandwidth_usage()