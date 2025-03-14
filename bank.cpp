// ====================================================================
//                           TGDK BFE LICENSE                         
// ====================================================================
#ifndef SOLANO_FINANCE_H
#define SOLANO_FINANCE_H

#include <iostream>
#include <vector>

class SolanoFinance {
public:
    struct DebtRecord {
        std::string debtor;
        double amount;
        bool paid;
    };

    struct LegalCase {
        std::string entity;
        std::string status;
        bool bankruptcyFiled;
    };

    std::vector<DebtRecord> debts;
    std::vector<LegalCase> legalCases;

    void recordDebt(std::string debtor, double amount);
    void fileBankruptcy(std::string entity);
    void interveneLegally(std::string entity, std::string status);
};

#endif