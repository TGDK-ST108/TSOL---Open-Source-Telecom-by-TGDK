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
| PublicTelemetryAPI                                                       
| © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.            
| Licensed under TGDK Open Source License (TSOL) - BFE Licensing.         
|                                                                         
| Permissions: Non-commercial use, modification, redistribution allowed.  
| Restrictions: Commercial use prohibited without written authorization.  
|=========================================================================*/

import requests

class PublicTelemetry:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_data(self, payload):
        response = requests.post(self.endpoint, json=payload)
        if response.ok:
            return response.json()
        else:
            return {"error": "Telemetry submission failed.", "status": response.status_code}