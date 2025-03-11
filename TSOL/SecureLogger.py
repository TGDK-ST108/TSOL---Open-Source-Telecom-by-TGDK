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

import logging
import hashlib

class TGDK_SecureLogger:
    def __init__(self, t_code_key, log_name='TGDK'):
        self.logger = logging.getLogger(log_name)
        handler = logging.FileHandler(f'{log_name}.log')
        handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s'))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        self.t_code_key = t_code_key

    def secure_log(self, message, level="INFO"):
        secured_message = self._t_code_hash(message)
        if level.upper() == "INFO":
            self.logger.info(secured_message)
        elif level.upper() == "ERROR":
            self.logger.error(secured_message)

    def _t_code_hash(self, message):
        hashed_msg = hashlib.sha384(f"{message}:{self.t_code_key}".encode()).hexdigest()
        return f"T-Code:{hashed_msg}"

# Example usage:
# logger = TGDK_SecureLogger(t_code_key="securekey123")
# logger.secure_log("System initialized.")