// ====================================================================
//                           TGDK BFE LICENSE                         
// ====================================================================
#ifndef FPMT_SOLANO_H
#define FPMT_SOLANO_H

#include <iostream>
#include <vector>

class FPMT_Solano {
public:
    struct Donation {
        std::string donor;
        double amount;
        std::string transactionID;
    };

    struct Request {
        std::string requester;
        double amount;
        std::string purpose;
        bool approved;
    };

    struct MemberEvaluation {
        std::string name;
        int socialScore, tendenciesScore, receptionScore;
        bool approved;
    };

    void processDonation(const std::string& donor, double amount, const std::string& transactionID);
    void submitRequest(const std::string& requester, double amount, const std::string& purpose);
    void evaluateMember(const std::string& name, int social, int tendencies, int reception);

private:
    std::vector<Donation> donations;
    std::vector<Request> requests;
    std::vector<MemberEvaluation> evaluations;
};

#endif