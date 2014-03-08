from collections import OrderedDict
from os import path
import json
import curses

# Order for officer list sort
officer_order = [
        "President",
        "Vice President",
        "Treasurer",
        "Secretary/ICC Rep.",
        "Enforcer"
        ]

# General member class
class Member(OrderedDict):
    memberCount = 0

    def __init__(self, first, last=None, email=None):
        super(Member, self).__init__()
        self["__type__"] = "member"
        self["first"] = first
        self["last"] = last
        self["email"] = email
        Member.memberCount += 1

    def __lt__(self, other):
       return self["last"] < other["last"]

    def __str__(self):
        return str(self.__dict__)

# Officer member class
class Officer(Member):
    officerCount = 0

    def __init__(self, first, last, email, position):
        Member.__init__(self, first, last, email)
        self["__type__"] = "officer"
        self["position"] = position

    def __lt__(self, other):
        return officer_order.index(self["position"]) < officer_order.index(other["position"])

    def __str__(self):
        return str(self.__dict__)

# Decode members json file
def decodeJson(fp, members, officers):
    json_dict = json.load(open(fp, 'r'))
    for i in json_dict:
        m = decodeMember(i)
        if type(m) is Member:
            members.append(m)
        elif type(m) is Officer:
            officers.append(m)

# Decode a single member json dictionary
def decodeMember(obj):
    if "__type__" in obj:
        if obj["__type__"] == 'member':
            return Member(obj["first"],obj["last"],obj["email"])
        elif obj["__type__"] == "officer":
            return Officer(obj["first"],obj["last"],obj["email"],obj["position"])

# -----------------------------------------------
# Command-line functions
# -----------------------------------------------
class MemberCMD():
    loop = True

# Print help
    def Help(self):
        print("[h] : Show this menu")
        print("[q] : Quit/cancel current command")
        print("[a] : Add a member/officer")
        print("[d] : Delete a member/offier")
        print("[l] : List all members")
        print("[o] : List all officers")

# Get input
    def Input(self, msg, ref):
        s = input(msg)
        if s is 'c':
            return False

# Parse command character
    def Parse(c):
        if c is 'h':
            self.Help()
        elif c is 'q':
            MemberCMD.loop = False
        elif c is 'a':
            MemberCMD.Add()
        elif c is 'd':
            MemberCMD.Delete()
        elif c is 'l':
            MemberCMD.ListMembers()
        elif c is 'o':
            MemberCMD.ListOfficers()
        else:
            print("Error: Unknown option \"%s\""%c)
            return False;

    def Add():
        officer = False
        c = ''
        print("Enter [c] to cancel")
        while True:
            if not MemberCMD.input("Officer? [y/n]: ", c):
                return
            elif c is 'y':
                officer = True
                break
            elif c is 'n':
                break
            else:
                print("Error: Unknown option \"%s\""%c)
        if not MemberCMD.input("First name: ", first):
            return
        if not MemberCMD.input("Last name: ", last):
            return
        if not MemberCMD.input("E-Mail: ", email):
            return
        print(first)
        print(last)
        print(email)

    def Delete():
        officer = False
        c = ''
        print("Enter [c] to cancel")
        while True:
            c = input("Officer? [y/n] :")

    def ListMembers():
        return 0

    def ListOfficers(self):
        return 0

    def Curses(*args):
        stdscr = curses.initscr()
        curses.endwin()

    def main(*args):
        MemberCMD.Curses()

# If called from command line
if __name__ == "__main__":
    m = MemberCMD()
    m.main("members.json")
