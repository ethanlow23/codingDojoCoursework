require 'rails_helper'
feature 'guest user creates a username' do
    before(:each) do
        visit root_path
    end
    scenario 'successfully creates a username' do
        fill_in 'first_name', with: 'Thomas'
        fill_in 'last_name', with: 'Thompson'
        fill_in 'username', with: 'username5'
        click_button 'Sign In'
        expect(page).to have_content 'Welcome Thomas'
        expect(page).to have_current_path(messages_path)
    end
    scenario 'unsuccessfully creates a username' do
        click_button 'Sign In'
        expect(current_path).to eq(root_path)
    end
    scenario 'does not fill out first name' do
        fill_in 'last_name', with: 'last'
        fill_in 'username', with: 'username'
        click_button 'Sign In'
        expect(page).to have_content "First name can't be blank"
    end
    scenario 'does not fill out last name' do
        fill_in 'first_name', with: 'first'
        fill_in 'username', with: 'username'
        click_button 'Sign In'
        expect(page).to have_content "Last name can't be blank"
    end
    scenario 'does not fill out username' do
        fill_in 'first_name', with: 'first'
        fill_in 'last_name', with: 'last'
        click_button 'Sign In'
        expect(page).to have_content "Username can't be blank"
    end
end