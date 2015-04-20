class Bill:

    all_bills = []
    bills_count = 0

    def __init__(self, amount):
        self.amount = amount
        Bill.all_bills.append(self)
        Bill.bills_count += 1

    def __str__(self):
        return str(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return int(self.amount)

    def __add__(self, other):
        return self.amount + other.amount

    @staticmethod
    def total_amount():
        return sum(int(x) for x in Bill.all_bills)

    @staticmethod
    def total_count():
        return int(Bill.bills_count)

    @staticmethod
    def bills_info():
        print("Here are all the bills:")
        for x in Bill.all_bills:
            print(x)


class BatchBill:

    def __init__(self, bill_list):
        self.bill_list = bill_list

    def __str__(self):
        output = ""
        for x in self.bill_list:
            output += str(x) + "\n"
        return output

    def __len__(self):
        #print("This batch has "+ str(len(self.bill_list)) + " amounts.")
        return len(self.bill_list)

    def total(self):
        return sum(int(x) for x in self.bill_list)

    def __getitem__(self, index):
        return self.bill_list[index]


class CashDesk:

    all_money = {}

    def __init__(self, moneys=0):
        self.moneys = 0

    def take_money(self, batchbill):
        if isinstance(batchbill, Bill):
            self.moneys = batchbill
            if str(batchbill) in CashDesk.all_money:
                CashDesk.all_money[str(batchbill)] += 1
            if str(batchbill) not in CashDesk.all_money:
                CashDesk.all_money.update({str(batchbill):1})
        if isinstance(batchbill, BatchBill):
            for x in batchbill:
                self.moneys += int(x)
                if str(x) in CashDesk.all_money:
                    CashDesk.all_money[str(x)] += 1
                if str(x) not in CashDesk.all_money:
                    CashDesk.all_money.update({str(x):1})

    @staticmethod
    def inspect():
        print("Current situation in our cashdesk:")
        for key,value in CashDesk.all_money.items():
            print(key+"$ - " + str(value))

    def __str__(self):
        return str(self.moneys)

    def total(self):
        return "We have currently " + str(self.moneys) + "$ in the desk"



