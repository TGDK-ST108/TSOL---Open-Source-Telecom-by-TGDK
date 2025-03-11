/*=========================================================================
| TGDK_AI_DataFormatter Module                                             
| © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.            
| Licensed under TGDK Open Source License (TSOL) - BFE Licensing.         
|                                                                         
| Permissions: Non-commercial use, modification, redistribution allowed.  
| Restrictions: Commercial use prohibited without written authorization.  
|=========================================================================*/

class DataFormatter:
    def to_json(self, data):
        return json.dumps(data, indent=2)

    def from_json(self, json_string):
        return json.loads(json_string)

    def validate_schema(self, data, schema):
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError as e:
            return False

# Example usage:
# formatter = DataFormatter()
# formatted_json = formatter.to_json({"key": "value"})