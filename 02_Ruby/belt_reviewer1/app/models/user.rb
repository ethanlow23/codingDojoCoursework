class User < ActiveRecord::Base
  has_secure_password
  has_many :events
  has_many :comments
  has_many :joins, dependent: :destroy
  has_many :events_joined, through: :joins, source: :event
  validates :first_name, :last_name, :email, :city, presence: true
  validates :email, uniqueness: true, format: { with: /\A[^@\s]+@([^@.\s]+\.)+[^@.\s]+\z/ }
  validates :state, length: {is: 2}
  #validates :password, confirmation: true
  before_create do
    self.email = email.downcase
  end
end
