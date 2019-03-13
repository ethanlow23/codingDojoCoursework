require 'rails_helper'

RSpec.describe User, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
  context 'With valid attributes' do
    it 'should save' do
      expect(build(:user)).to be_valid
    end
  end
  context 'With invalid attributes' do
    it 'should not save if first name is blank' do
      expect(build(:user, first_name: '')).to be_invalid
    end
    it 'should not save if last_name is blank' do
      expect(build(:user, last_name: '')).to be_invalid
    end
    it 'should not save if username is blank' do
      expect(build(:user, username: '')).to be_invalid
    end
    it 'should not save if username is not longer than 5 characters' do
      expect(build(:user, username: 'name')).to be_invalid
    end
  end
end
