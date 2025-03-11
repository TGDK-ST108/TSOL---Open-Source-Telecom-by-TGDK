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

/*=========================================================================
| TGDK_TelecomLogger Module                                                
| © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.            
| Licensed under TGDK Open Source License (TSOL) - BFE Licensing.         
|========================================================================*/

import logging
from datetime import datetime

class TelecomLogger:
    def __init__(self, logfile="tgdk_telecom.log"):
        self.logfile = logfile

    def log_event(self, message, level="INFO"):
        with open("TGDK_Log.txt", "a") as logfile:
            logfile.write(f"{level}: {message}\n")
            
    def info(self, message):
        self.log("INFO", message)
        
    def error(self, message):
        self.log("ERROR", message)