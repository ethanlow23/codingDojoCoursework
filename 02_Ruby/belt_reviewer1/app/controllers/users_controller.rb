class UsersController < ApplicationController
    def index
        render "users/index.html.erb"
    end
    def register
        # @user = User.new(user_params)
        # if @user.save
        #     session[:user_id] = @user.id
        #     redirect_to events_path
        # else
        #     flash[:errors] = @user.errors.full_messages
        #     redirect_to root_path
        # end
        user = User.create(user_params)
        if !user.valid?
            flash[:errors] = user.errors.full_messages
            redirect_to root_path
        else
            session[:user_id] = user.id
            redirect_to events_path
        end
    end
    def login
        if User.find_by_email(params[:user][:email]).try(:authenticate, params[:user][:password])
            session[:user_id] = User.find_by_email(params[:user][:email]).id
            redirect_to events_path
        else
            flash[:errors] = ["Invalid Combination"]
            redirect_to root_path
        end
    end
    def destroy
        session[:user_id] = nil
        redirect_to root_path
    end
    def edit
        render "users/edit.html.erb"
    end
    def update
        update_user = User.find(current_user.id)
        update_user.update(user_params)
        if !update_user.valid?
            flash[:errors] = update_user.errors.full_messages
            redirect_to "/users/#{current_user.id}"
        else
            redirect_to events_path
        end
    end
    private
    def user_params
        params.require(:user).permit(:first_name, :last_name, :email, :city, :state, :password, :password_confirmation)
    end
end
