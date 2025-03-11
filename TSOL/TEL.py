# ============================================================================
#                    TGDK OPEN SOURCE LICENSE (TSOL)
#                 GLOBAL EDITION – BROADCASTED FEE ENTRY (BFE)
#
# © 2025 Sean Tichenor, TGDK & OliviaAI. All Rights Reserved.
#
# Security Framework: TichenorCode (T-Code)
# Exclusively developed by Sean Tichenor for TGDK.
#
# Permissions: Non-commercial use, modification, redistribution allowed.
# Attribution required for all derivatives.
#
# Restrictions:
#   - Commercial use prohibited without explicit authorization.
#   - Unauthorized duplication or modification of TichenorCode prohibited.
#
# Licensed under TSOL/BFE Licensing.
# Full details at: https://olivia-tgdk.com/license
# ============================================================================

import hashlib
import datetime

class TelecomEventLogger:
    def __init__(self, log_file, t_code_key):
        self.log_file = log_file
        self.t_code_key = t_code_key

    def log_event(self, event_type, event_details):
        timestamp = datetime.datetime.utcnow().isoformat()
        entry = f"{timestamp} [{event_type}] {event_details}"
        integrity_hash = self._generate_hash(entry)
        with open(self.log_file, 'a') as log:
            log.write(f"{entry} | Hash: {integrity_hash}\n")

    def _generate_hash(self, entry):
        combined = f"{entry}:{self.t_code_key}"
        return hashlib.sha384(combined.encode()).hexdigest()

# Example Usage:
# logger = TelecomEventLogger("events.log", t_code_key="securekey123")
# logger.log_event("INFO", "System initialized successfully.")