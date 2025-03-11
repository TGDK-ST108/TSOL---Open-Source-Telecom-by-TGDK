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