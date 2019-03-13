class ControllersController < ApplicationController
    def index
        render text: "what do you want me to say"
    end
    def hello
        render text: "hello"
    end
    def say_hello
        render text: "saying hello"
    end
    def hello_joe
        render text: "saying hello joe"
    end
    def hello_michael
        redirect_to "/say/hello/joe"
    end

    def times
        unless session.key?('count')
            session['count'] = 0
        end
        session['count'] += 1
        render text: "you have visited this page #{session['count']}"
    end
    def restart_times
        session.clear
        render text: "destroyed the session"
    end
end
