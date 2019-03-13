class BankAccount
    attr_reader :account_number, :checking, :savings
    private
        def generate_account_num
            rand(10 ** 16)
        end
    public
    def initialize
        @account_number = generate_account_num
        @checking = 0
        @savings = 0
        @interest_rate = 0.01
    end
    def deposit(account, amount)
        if account == "checking"
            @checking += amount
        elsif account == "savings"
            @savings += amount
        else
            "not a valid account"
        end
        self
    end
    def withdraw(account, amount)
        if account == "checking"
            if amount > @checking
                raise StandardError
            else
                @checking -= amount
            end
        elsif account == "savings"
            if amount > @savings
                raise StandardError
            else
                @savings -= amount
            end
        else
            "not a valid account"
        end
        self
    end
    def total_amount
        @checking + @savings
    end
    def account_information
        "#{@account_number}, #{total_amount}, #{@checking}, #{@savings}, #{@@interest_rate}"
    end
end
