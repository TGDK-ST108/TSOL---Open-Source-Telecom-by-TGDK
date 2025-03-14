# ====================================================================
#                           TGDK BFE LICENSE                         
# ====================================================================
#                          BROADCASTED FEE ENTRY                       
# ====================================================================
# LICENSE HOLDER:              |  Sean Tichenor                        
# LICENSE CODE:                |  BFE-TGDK-022ST                       
# DATE OF ISSUANCE:            |  March 10, 2025                       
# LICENSE STATUS:              |  ACTIVE                                
# ISSUING AUTHORITY:           |  TGDK Licensing Authority             
# ====================================================================
# DESCRIPTION:  
# This license certifies that Sean Tichenor is granted the Broadcasted  
# Fee Entry (BFE) License under TGDK regulations. All applicable terms,  
# conditions, and authorizations are in effect as of the issuance date.  
# ====================================================================
# NOTICE:  
# Unauthorized duplication, modification, or redistribution of this license  
# is strictly prohibited under TGDK regulatory compliance.                 
# ====================================================================
#                          FOR OFFICIAL USE ONLY                        
# ====================================================================

#include "SolanoFinance.h"

void SolanoFinance::recordDebt(std::string debtor, double amount) {
    debts.push_back({debtor, amount, false});
    std::cout << "Debt recorded: " << debtor << " owes $" << amount << std::endl;
}

void SolanoFinance::fileBankruptcy(std::string entity) {
    legalCases.push_back({entity, "Under Bankruptcy Review", true});
    std::cout << "Bankruptcy filed for " << entity << std::endl;
}

void SolanoFinance::interveneLegally(std::string entity, std::string status) {
    legalCases.push_back({entity, status, false});
    std::cout << "Legal intervention for " << entity << " - Status: " << status << std::endl;
}