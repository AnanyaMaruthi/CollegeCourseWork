class CallDetail:

    def __init__(self, detailString):
        detailString = detailString.split(",")
        self.caller = detailString[0]
        self.receiver = detailString[1]
        self.duration = detailString[2]
        self.callType = detailString[3]

    def getData(self):
        print("Caller:", self.caller)
        print("Receiver:", self.receiver)
        print("Call Duration:", self.duration)
        print("Call Type:", self.callType)


class Util:

    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for call in list_of_call_string:
            callDetailObject = CallDetail(call)
            self.list_of_call_objects.append(callDetailObject)

    def showAllCalls(self):
        i = 1
        for call in self.list_of_call_objects:
            print("Call", i, ":")
            call.getData()
            i += 1


call='9990000001,9330000001,23,STD'

call2='9990000001,9330000002,54,Local'

call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]

util = Util()
util.parse_customer(list_of_call_string)
util.showAllCalls()