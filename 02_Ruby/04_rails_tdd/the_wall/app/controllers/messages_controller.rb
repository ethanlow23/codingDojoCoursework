class MessagesController < ApplicationController
    def register
        session[:user] = nil
        render 'messages/register.html.erb'
    end
    def register_user
        @user = User.new(params.require(:user).permit(:first_name, :last_name, :username))
        if @user.save
            session[:user] = @user unless session.key?(:user)
            redirect_to messages_path
        else
            #errors we need to code later
            flash[:notice] = @user.errors.full_messages
            redirect_to root_path
        end
    end
    def index
        @messages = Message.order('created_at DESC')
        @comments = Comment.order('created_at ASC')
    end
    def create
        @message = User.find(session[:user]["id"]).messages.new(params.require(:message).permit(:content))
        if @message.save
            redirect_to messages_path
        else
            flash[:msg_error] = @message.errors.full_messages
            redirect_to messages_path
        end
    end
    def comment
        @comment = User.find(session[:user]["id"]).comments.new(params.require(:comment).permit(:content, :message_id))
        if @comment.save
            redirect_to messages_path
        else
            flash[:comment_error] = @comment.errors.full_messages
            redirect_to messages_path
        end
    end
end
