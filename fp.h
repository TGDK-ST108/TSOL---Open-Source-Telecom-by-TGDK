// ====================================================================
//                           TGDK BFE LICENSE                         
// ====================================================================
#ifndef FPMT_SOLANO_H
#define FPMT_SOLANO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    char name[50];
    int social_habits_score;
    int tendencies_score;
    int receptionary_score;
    int evaluation_status;
} MemberEvaluation;

void processDonation(char donor[], float amount, char transactionID[]);
void submitRequest(char requester[], float amount, char purpose[]);
void evaluateMember(char name[], int social, int tendencies, int receptionary);

#endif