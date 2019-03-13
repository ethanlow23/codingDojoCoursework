require_relative 'apple_tree'
RSpec.describe AppleTree do
    before(:each) do
        @tree1 = AppleTree.new(1)
    end
    it 'has getter and setter for age attribute' do
        @tree1.age = 3
        expect(@tree1.age).to eq(3)
    end
    it 'cannot set height attribute' do
        expect{@tree1.height = 50}.to raise_error(NoMethodError)
    end
    it 'cannot set the apple count attribute' do
        expect{@tree1.apple_count = 20}.to raise_error(NoMethodError)
    end
    it 'has year gone by method to add one year to age, increase height by 10% and raise apple count by two' do
        expect(@tree1.year_gone_by).to eq ("age: 2, height: 11.0, count: 7")
    end
    it 'has pick apples method to take all apples off the tree' do
        expect(@tree1.pick_apples).to eq(0)
    end
    
end