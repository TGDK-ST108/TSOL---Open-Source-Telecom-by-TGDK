// ====================================================================
//                           TGDK BFE LICENSE                         
// ====================================================================

import java.util.ArrayList;

class SolanoFinance {
    static class DebtRecord {
        String debtor;
        double amount;
        boolean paid;
        
        DebtRecord(String debtor, double amount) {
            this.debtor = debtor;
            this.amount = amount;
            this.paid = false;
        }
    }

    static class LegalCase {
        String entity;
        String status;
        boolean bankruptcyFiled;
        
        LegalCase(String entity, String status, boolean bankruptcyFiled) {
            this.entity = entity;
            this.status = status;
            this.bankruptcyFiled = bankruptcyFiled;
        }
    }

    ArrayList<DebtRecord> debts = new ArrayList<>();
    ArrayList<LegalCase> legalCases = new ArrayList<>();

    public void recordDebt(String debtor, double amount) {
        debts.add(new DebtRecord(debtor, amount));
        System.out.println("Debt Recorded: " + debtor + " owes $" + amount);
    }

    public void fileBankruptcy(String entity) {
        legalCases.add(new LegalCase(entity, "Under Bankruptcy Review", true));
        System.out.println("Bankruptcy Filed for " + entity);
    }
}