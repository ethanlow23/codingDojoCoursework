require_relative 'bank_account'
RSpec.describe BankAccount do
    before(:each) do
        @account1 = BankAccount.new
        @account1.deposit('checking', 100).deposit('savings', 500).withdraw('checking', 50).withdraw('savings', 200)
    end
    it 'has a getter method for account number attribute' do
        expect(@account1.checking).to eq(50)
    end
    it 'has a getter method for total account balance' do
        expect(@account1.total_amount).to eq(350)
    end
    it 'has a function to withdraw cash' do
        @account1.withdraw('checking', 25)
    end
    it 'cannot withdraw more money than in the account' do
        expect{@account1.withdraw('checking', 1000)}.to raise_error(StandardError)
    end
    it 'cannot retrieve total number of bank accounts' do
        expect{@account1.accounts}.to raise_error(NoMethodError)
    end
    it 'cannot set interest rate' do
        expect{@account1.interest_rate = 1.0}.to raise_error(NoMethodError)
    end
end