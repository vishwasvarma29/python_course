data={
    '1234':{'balance':45678,'pin':123,'history':[]},
    '1256':{'balance':45678,'pin':123,'history':[]},
    '9865':{'balance':45678,'pin':123,'history':[]},
    '8903':{'balance':45678,'pin':123,'history':[]},''
    '7843':{'balance':45678,'pin':123,'history':[]},
}
acc_num=None
login_status=False
def Welcome():
    print('Welcome to the ATM',enter(40,'-'))
def menu():
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Transaction History')
    print('0. Exit')

def login(acc,pin):
    if acc in data:
        if data[acc] ['pin']==pin:
            