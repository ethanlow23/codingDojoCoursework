class UsersController < ApplicationController
    def index
        render json: User.all
    end
    def new
        render "users/new"
    end
    def first_user
        render json: User.first
    end
    def edit_user1
        @user1 = User.first
        render "users/edit_user1"
    end
    def create
        User.create(name:params['name'])
        redirect_to "/users"
    end
    def total
        render text: "The total number of users: #{User.count}"
    end
end
