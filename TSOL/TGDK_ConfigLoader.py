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

import yaml

class ConfigLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_config(self):
        with open(self.filepath, 'r') as file:
            return yaml.safe_load(file)

    def update_config(self, key, value):
        config = self.load_config()
        config[key] = value
        with open(self.filepath, 'w') as file:
            yaml.safe_dump(config, file, default_flow_style=False)