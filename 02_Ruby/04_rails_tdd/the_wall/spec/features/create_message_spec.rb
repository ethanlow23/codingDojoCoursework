require 'rails_helper'
feature 'user logs on' do
    before(:each) do
        visit root_path
        fill_in 'first_name', with: 'Thomas'
        fill_in 'last_name', with: 'Thompson'
        fill_in 'username', with: 'username5'
        click_button 'Sign In'
    end
    scenario 'successfully creates a message' do
        fill_in 'content', with: 'this is my first message on this site'
        click_button 'Post a Message'
        expect(page).to have_current_path(messages_path)
        expect(page).to have_content 'this is my first message on this site'
    end
    scenario 'unsuccessfully creates a message' do
        fill_in 'content', with: ''
        click_button 'Post a Message'
        expect(page).to have_current_path(messages_path)
        expect(page).to have_content "Content can't be blank"
    end
    scenario 'logs out' do
        expect(page).to have_link 'Log Out'
        click_link 'Log Out'
        expect(page).to have_current_path(root_path)
    end
end