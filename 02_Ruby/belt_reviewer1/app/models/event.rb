class Event < ActiveRecord::Base
  belongs_to :user
  has_many :comments
  has_many :joins, dependent: :destroy
  has_many :users_joined, through: :joins, source: :user
  validates :name, :city, :state, presence: true
  
  validate :future_event
  private
  def future_event
    if date == nil
      errors.add(:date, "Can't be empty")
    elsif date < Time.now
      errors.add(:date, "Can't be in the past!")
    end
  end
end
