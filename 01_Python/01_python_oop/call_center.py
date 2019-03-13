class Call(object):
    def __init__(self, unique_id, caller_name, caller_number, timeOfCall, reasonForCall):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.timeOfCall = timeOfCall
        self.reasonForCall = reasonForCall

    def display(self):
        print self.unique_id, self.caller_name, self.caller_number, self.timeOfCall, self.reasonForCall

class CallCenter(object):
    def __init__(self, calls, queue_size):
        self.calls = []
        self.queue_size = len(self.calls)
    
    def add(self):
        self.calls.append(Call(object))

    def remove(self):
        self.calls.pop(0)

    def info(self):
        for i in range(len(self.calls)):
            print self.calls[i]

call1 = Call('1', 'john doe', '555-0000', '1 minute', 'nothing')