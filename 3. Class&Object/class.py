class Phone:
    brand = "Samsung"
    color = "Blue"
    print = 27000
    features = ['cammera', 'speaker', 'bluetooth']

    def call(self):
        print("calling me")
    
    def send_sms(self, text, number):
        sms = f'sending sms to {number}, your sms is: {text}'
        return sms

my_phone = Phone()
print(my_phone.brand)
print(my_phone.features)
my_phone.call()
print(my_phone.send_sms("ki r bolbo tuamy", 1235))