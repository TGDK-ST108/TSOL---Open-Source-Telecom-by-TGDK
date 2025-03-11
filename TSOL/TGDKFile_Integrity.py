# ============================================================================
#                             TGDK OPEN SOURCE LICENSE (TSOL)                
#                         GLOBAL VERSION – BROADCASTED FEE ENTRY (BFE)        
#                                                                            
# LICENSE HOLDER:       Sean Tichenor                                        
# LICENSE CODE:         TGDK-BFE-175943-2025                                 
# ISSUING AUTHORITY:    TGDK Licensing Authority                             
# VALIDITY:             ACTIVE                                               
# YEAR:                 2025                                                  
#                                                                             
# Permissions: Non-commercial use, modification, redistribution allowed.      
# Restrictions: Commercial use prohibited without explicit written consent.   
# Unauthorized commercial usage, duplication, or redistribution of this code  
# or license is strictly prohibited.                                          
#                                                                             
# Original Work © 2025 TGDK & Sean Tichenor.                                 
# Licensed under the TGDK Open Source License (TSOL), structured under BFE.   
#                                                                             
# Official License Registry: https://olivia-tgdk.com/license                  
# ============================================================================

# ============================================================================
#                          TGDK OPEN SOURCE LICENSE (TSOL)
#                      GLOBAL VERSION – BROADCASTED FEE ENTRY
#
# © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.
#
# Permissions: Non-commercial use, modification, redistribution allowed.
# Restrictions: Commercial use prohibited without explicit authorization.
# ============================================================================

import hashlib

class FileIntegrityChecker:
    @staticmethod
    def get_sha256(file):
        import hashlib
        hasher = hashlib.sha256()
        with open(file, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def verify_hash(self, file, expected_hash):
        return self.get_sha256(file) == expected_hash