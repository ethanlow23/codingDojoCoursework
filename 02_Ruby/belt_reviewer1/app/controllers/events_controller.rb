class EventsController < ApplicationController
    def index
        @events = Event.all
        render "events/index.html.erb"
    end
    def create
        @event = User.find(current_user.id).events.new(event_params)
        unless @event.save
            flash[:errors] = @event.errors.full_messages
        end
        redirect_to events_path
    end
    def show
        @show_event = Event.find(params[:event_id])
        @comments = Event.find(params[:event_id]).comments
        render "events/show.html.erb"
    end
    def edit
        @edit_event = Event.find(params[:event_id])
        render "events/edit.html.erb"
    end
    def update
        update_event = User.find(current_user.id).events.update(params[:event_id], event_params)
        if update_event.valid?
            redirect_to events_path
        else
            flash[:errors] = update_event.errors.full_messages
            redirect_to "/events/#{params[:event_id]}/edit"
        end
    end
    def destroy
        Event.find(params[:event_id]).destroy
        redirect_to events_path
    end
    def join
        User.find(current_user.id).joins.create(event:Event.find(params[:event_id]))
        redirect_to events_path
    end
    def unjoin
        User.find(current_user.id).joins.find_by(event:Event.find(params[:event_id])).destroy
        redirect_to events_path
    end
    def comment
        @new_comment = Event.find(params[:event_id]).comments.new(content: params[:content], user: User.find(current_user.id))
        unless @new_comment.save
            flash[:errors] = @new_comment.errors.full_messages
        end
        redirect_to "/events/#{params[:event_id]}"
    end
    private
    def event_params
        params.require(:event).permit(:name, :date, :city, :state)
    end
end
