class User < ActiveRecord::Base
    validates :first_name, :last_name, presence: true
    validates :email, uniqueness: true, format: { with: /\A[^@\s]+@([^@.\s]+\.)+[^@.\s]+\z/ }
end
