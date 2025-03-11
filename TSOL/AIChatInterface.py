#ifndef TGDK_BFE_LICENSE_H
#define TGDK_BFE_LICENSE_H

// ================================================================
//                         TGDK BFE LICENSE                         
// ================================================================

// ====================== BROADCASTED FEE ENTRY =====================
// This section clearly defines the type of license being issued.

// ================================================================
// LICENSE HOLDER:            |  Sean Tichenor
// ================================================================
// The name of the individual to whom this license is issued.

// LICENSE CODE:              |  BFE-TGDK-500ST
// ================================================================
// A unique identifier assigned to this specific license.

// DATE OF ISSUANCE:          |  March 10, 2025
// ================================================================
// The official date on which this license was issued.

// LICENSE STATUS:            |  ACTIVE
// ================================================================
// Indicates whether the license is currently valid or inactive.

// ISSUING AUTHORITY:         |  TGDK Licensing Authority
// ================================================================
// The organization responsible for issuing and regulating the license.

// ======================= LICENSE DESCRIPTION ======================
// DESCRIPTION:
// This license certifies that Sean Tichenor is granted the Broadcasted  
// Fee Entry (BFE) License under TGDK regulations. All applicable terms,  
// conditions, and authorizations are in effect as of the issuance date.
// ================================================================
// This section provides a brief overview of the license's purpose 
// and its regulatory framework.

// ========================== NOTICE =============================
// NOTICE:  
// Unauthorized duplication, modification, or redistribution of this license  
// is strictly prohibited under TGDK regulatory compliance.  
// ================================================================
// A legal disclaimer ensuring compliance and protection against 
// unauthorized use of the license.

// ======================== FOR OFFICIAL USE ONLY =======================
// ================================================================
// This indicates that the document is legally binding and should
// only be accessed or modified by authorized personnel.

#endif // TGDK_BFE_LICENSE_H

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
