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
|                       TGDK OPEN SOURCE LICENSE (TSOL)                   
|                       GLOBAL VERSION - BFE LICENSE                      
|                                                                         
|   © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.          
|                                                                         
|   Permissions: Non-commercial use, modification, redistribution allowed.
|   Restrictions: Commercial use prohibited without written authorization.
|   Original Work: © 2025 TGDK & Sean Tichenor. All rights reserved.     
|=========================================================================*/

import json
import yaml

class GenericParser:
    @staticmethod
    def parse_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def parse_yaml(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

# Example:
# parser = GenericParser()
# data = parser.load_yaml("config.yaml")