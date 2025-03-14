# ====================================================================
#                           TGDK BFE LICENSE                         
# ====================================================================

class FPMT_Solano
  attr_accessor :donations, :requests, :evaluations

  def initialize
    @donations = []
    @requests = []
    @evaluations = []
  end

  def process_donation(donor, amount, transaction_id)
    @donations << { donor: donor, amount: amount, transaction_id: transaction_id }
    puts "Donation received from #{donor}: $#{amount} - Transaction ID: #{transaction_id}"
  end

  def submit_request(requester, amount, purpose)
    @requests << { requester: requester, amount: amount, purpose: purpose, approved: false }
    puts "Request submitted by #{requester} for $#{amount} - Purpose: #{purpose}"
  end

  def evaluate_member(name, social, tendencies, reception)
    approved = social >= 5 && tendencies >= 5 && reception >= 5
    @evaluations << { name: name, social: social, tendencies: tendencies, reception: reception, approved: approved }
    puts "Evaluation recorded for #{name} - Status: #{approved ? 'Approved' : 'Pending'}"
  end
end

# Example Usage
fpmt = FPMT_Solano.new
fpmt.process_donation("Alice", 500.00, "TXN001")
fpmt.submit_request("Monastery A", 1500.00, "Food supplies")
fpmt.evaluate_member("John Doe", 7, 5, 8)