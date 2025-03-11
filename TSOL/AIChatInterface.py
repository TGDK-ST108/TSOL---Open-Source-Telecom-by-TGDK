/*=========================================================================
|                       TGDK OPEN SOURCE LICENSE (TSOL)                   
|                       GLOBAL VERSION - BFE LICENSE                      
|                                                                         
|   © 2025 Sean Tichenor, TGDK, & OliviaAI. All Rights Reserved.          
|                                                                         
|   Permissions: Non-commercial use, modification, redistribution allowed.
|   Restrictions: Commercial use prohibited without written authorization.
|   Original Work: © 2025 TGDK & Sean Tichenor. Licensed under TSOL - BFE.
|=========================================================================*/

# AIChatInterface.py

class AIChatInterface:
    def __init__(self, model_name):
        self.model = load_model(model=model_name)
    
    def send_query(self, query: str):
        response = self.model.generate_response(query=query)
        return response

    def format_response(self, response):
        return {"status": "success", "content": response}

# Example usage:
# ai = AIChatInterface("OliviaBasic")
# response = ai.send_query("Hello, OliviaAI?")
