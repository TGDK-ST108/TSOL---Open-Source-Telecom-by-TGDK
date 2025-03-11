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
#                             TGDK OPEN SOURCE LICENSE (TSOL)                
#                         GLOBAL VERSION – BROADCASTED FEE ENTRY              
#                                                                             
# © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.                
# Licensed under TSOL (BFE Licensing).                                        
# ============================================================================

import json
from jsonschema import validate, ValidationError

class DataFormatter:
    def serialize(self, data):
        return json.dumps(data, indent=2)

    def deserialize(self, json_data):
        return json.loads(json_data)

    def validate_data(self, data, schema):
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError:
            return False