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

import socket

class NetworkStatus:
    def check_host(self, host, port):
        try:
            socket.create_connection((host, port), timeout=5)
            return True
        except socket.error:
            return False

    def check_internet(self):
        return self.check_host("8.8.8.8", 53)