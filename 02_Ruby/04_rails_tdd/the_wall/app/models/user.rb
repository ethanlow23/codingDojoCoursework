class User < ActiveRecord::Base
    has_many :messages, dependent: :destroy
    has_many :comments, dependent: :destroy
    validates :first_name, :last_name, :username, presence: true
    validates :username, uniqueness: true, length: {minimum: 6}
end
