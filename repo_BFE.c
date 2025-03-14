// ====================================================================
//                           TGDK BFE LICENSE                         
// ====================================================================
//                          BROADCASTED FEE ENTRY                       
// ====================================================================
// LICENSE HOLDER:              |  Sean Tichenor                        
// LICENSE CODE:                |  BFE-TGDK-022ST                       
// DATE OF ISSUANCE:            |  March 10, 2025                       
// LICENSE STATUS:              |  ACTIVE                                
// ISSUING AUTHORITY:           |  TGDK Licensing Authority             
// ====================================================================
// DESCRIPTION:  
// This global header ensures uniform data structures and function 
// declarations across all files in the FPMT Solano Framework repository.  
// ====================================================================
// NOTICE:  
// Unauthorized duplication, modification, or redistribution of this license  
// is strictly prohibited under TGDK regulatory compliance.                 
// ====================================================================
//                          FOR OFFICIAL USE ONLY                        
// ====================================================================

#ifndef FPMT_GLOBAL_H
#define FPMT_GLOBAL_H

#define MAX_RECORDS 100

typedef struct {
    char donor[50];
    float amount;
    char transactionID[64];
} Donation;

typedef struct {
    char requester[50];
    float requested_amount;
    char purpose[100];
    int approved;
} Request;

typedef struct {
    char recipient[50];
    float amount;
    char verificationID[64];
} Provision;

typedef struct {
    char name[50];
    int social_habits_score;
    int tendencies_score;
    int receptionary_score;
    int evaluation_status;
} MemberEvaluation;

void processDonation(char donor[], float amount, char transactionID[]);
void submitRequest(char requester[], float amount, char purpose[]);
void approveRequest(int requestID);
void distributeProvision(char recipient[], float amount, char verificationID[]);
void evaluateMember(char name[], int social, int tendencies, int receptionary);
void displayWorkflowSubmissions();

#endif // FPMT_GLOBAL_H