require 'rails_helper'

RSpec.describe Message, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
  context 'With valid attributes' do
    it 'should save' do
      expect(build(:message)).to be_valid
    end
  end
  context 'With invalid attributes' do
    it 'should not save if content field is blank' do
      expect(build(:message, content: '')).to be_invalid
    end
    it 'should not save if content field is not longer than 10 characters' do
      expect(build(:message, content: 'invalid')).to be_invalid
    end
    it 'should not save if user field is blank' do
      expect(build(:message, user: nil)).to be_invalid
    end
  end
end
