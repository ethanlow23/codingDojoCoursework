class SurveysController < ApplicationController
    def index
        render "surveys/index.html.erb"
    end
    def info
        session[:survey] = params[:survey]
        session[:count] = 0 unless session.key?(:count)
        session[:count] += 1
        flash[:success] = "Thanks for submitting this form. You have submitted this form #{session[:count]} times now"
        redirect_to "/result"
    end
    def result
        render "surveys/result.html.erb"
    end
end
