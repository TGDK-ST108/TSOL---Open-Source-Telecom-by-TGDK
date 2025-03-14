// ====================================================================
//                           TGDK BFE LICENSE                         
// ====================================================================

import java.util.ArrayList;

class FPMT_Solano {
    static class Donation {
        String donor;
        double amount;
        String transactionID;
        
        Donation(String donor, double amount, String transactionID) {
            this.donor = donor;
            this.amount = amount;
            this.transactionID = transactionID;
        }
    }

    static class Request {
        String requester;
        double amount;
        String purpose;
        boolean approved;
        
        Request(String requester, double amount, String purpose) {
            this.requester = requester;
            this.amount = amount;
            this.purpose = purpose;
            this.approved = false;
        }
    }

    static class MemberEvaluation {
        String name;
        int socialScore, tendenciesScore, receptionScore;
        boolean approved;
        
        MemberEvaluation(String name, int social, int tendencies, int reception) {
            this.name = name;
            this.socialScore = social;
            this.tendenciesScore = tendencies;
            this.receptionScore = reception;
            this.approved = (social >= 5 && tendencies >= 5 && reception >= 5);
        }
    }

    ArrayList<Donation> donations = new ArrayList<>();
    ArrayList<Request> requests = new ArrayList<>();
    ArrayList<MemberEvaluation> evaluations = new ArrayList<>();

    public void processDonation(String donor, double amount, String transactionID) {
        donations.add(new Donation(donor, amount, transactionID));
        System.out.println("Donation received from " + donor + ": $" + amount);
    }

    public void submitRequest(String requester, double amount, String purpose) {
        requests.add(new Request(requester, amount, purpose));
        System.out.println("Request submitted by " + requester + " for $" + amount);
    }

    public void evaluateMember(String name, int social, int tendencies, int reception) {
        evaluations.add(new MemberEvaluation(name, social, tendencies, reception));
        System.out.println("Evaluation recorded for " + name);
    }
}