FactoryGirl.define do
  factory :message do
    content "This is my message"
    user
  end
end
