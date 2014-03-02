from collections import OrderedDict

# Member base class
# class Member():

#     memberCount = 0

#     def __init__(self, first, last=None, email=None):
#         self.first = first
#         self.last = last
#         self.email = email
#         Member.memberCount += 1

#     def __str__(self):
#         return str(self.__dict__)

#     def __iter__(self):
#         return iter(self.__dict__.items())

# # Officer class
# class Officer(Member):
#     def __init__(self, first, last=None, email=None, position=None):
#         super(Officer, self).__init__(first, last, email)
#         self.position = position

# members = {
#     'swar_mary':        Officer("Mary","Swar","socalswar@gmail.com","President"),
#     'bayley_charles':   Officer("Charles","Bayley","cbayley95@gmail.com","Vice President"),
#     'doan_quan':        Officer("Quan","Doan","quandoan04@yahoo.com","Treasurer"),
#     'olsson_nils':      Officer("Nils","Olsson","nilso@enosis.net","Secretary/ICC Rep.")
# }

# for k, v in members.items():
#     if type(v) is Officer:
#         print(v)

class Member(OrderedDict):

    memberCount = 0

    def __init__(self, first, last=None, email=None):
        OrderedDict({'first':first,'last':last,'email':email})
        Member.memberCount += 1

    def __get__(self, key):
        return OrderedDict[key]

    # def __str__(self):
    #     return 

print(OrderedDict({'first':"Nils",'last':"Olsson",'email':"nilso@enosis.net"}))

m = Member("Nils","Olsson","nilso@enosis.net")

print(m['first'])

# members_old = [
#         (
#         "Swar",
#         "Mary",
#         "socalswar@gmail.com",
#         "President"
#         ),
#         (
#         "Bayley",
#         "Charles",
#         "cbayley95@gmail.com",
#         "Vice President"
#         ),
#         (
#         "Doan",
#         "Quan",
#         "quandoan04@yahoo.com",
#         "Treasurer"
#         ),
#         (
#         "Olsson","Nils",
#         "nilso@enosis.net",
#         "Secretary/ICC Rep."
#         ),
#         (
#         "Cortopasi",
#         "Foryst",
#         "shadow_ridley@yahoo.com",
#         "Enforcer"
#         ),
#         (
#         "Caragay",
#         "Virgil",
#         "v.caragay21@gmail.com"
#         ),
#         (
#         "Clements",
#         "Joseph",
#         "josephmclements@gmail.com"
#         ),
#         (
#         "Yu",
#         "Adam",
#         "yuadam108108@yahoo.com"
#         ),
#         (
#         "???",
#         "Andrey",
#         "munky8970@hotmail.com"
#         ),
#         (
#         "???",
#         "Devon",
#         "DMSallume@gmail.com"
#         ),
#         (
#         "???",
#         "Michael",
#         "elminc15@yahoo.com"
#         )
# ]