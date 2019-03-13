class RpgController < ApplicationController
    def index
        render "rpg/index.html.erb"
    end
    def gold
        session[:gold] = 0 unless session.key?(:gold)
        session[:activities] = [] unless session.key?(:activities)
        if params[:get_gold] == "farm"
            rand_num = (10 + rand(11))
            session[:gold] += rand_num
            session[:activities].insert(0, "Entered farm: earned #{rand_num} golds " + DateTime.now.strftime("%Y/%m/%d %H:%M %P"))
        elsif params[:get_gold] == "cave"
            rand_num = (5 + rand(6))
            session[:gold] += rand_num
            session[:activities].insert(0, "Entered cave: earned #{rand_num} golds " + DateTime.now.strftime("%Y/%m/%d %H:%M %P"))
        elsif params[:get_gold] == "house"
            rand_num = (2 + rand(6))
            session[:gold] += rand_num
            session[:activities].insert(0, "Entered house: earned #{rand_num} golds " + DateTime.now.strftime("%Y/%m/%d %H:%M %P"))
        else #params[:get_gold] == "casino"
            rand_num = (-50 + rand(101))
            session[:gold] += rand_num
            session[:activities].insert(0, "Entered casino: earned #{rand_num} golds " + DateTime.now.strftime("%Y/%m/%d %H:%M %P"))
        end
        redirect_to "/"
    end
end
