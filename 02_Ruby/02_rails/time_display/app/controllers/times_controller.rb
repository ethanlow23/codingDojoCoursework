class TimesController < ApplicationController
  def main
    @date = DateTime.now.in_time_zone("Pacific Time (US & Canada)").strftime("%b %d, %Y")
    @time = DateTime.now.in_time_zone("Pacific Time (US & Canada)").strftime("%l:%M %p")
    render "times/main.html.erb"
  end
end