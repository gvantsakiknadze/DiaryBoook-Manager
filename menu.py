import sys
import json

from diarybook import Diary, DiaryBook
from Users import Users
from util import read_from_json_into_application


class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()
        self.users = Users()
        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            '5': self.sort_diaries,
            '6': self.quit
        }
        self.email=""
        self.password=""

    def display_menu(self):
        print("""
            DiaryManager Menu By Skillwill
            1.Show diaries
            2.Add diaries
            3.Search in diaries
            4.Populate Database
            5.Sort diaries
            6.Quit program
            """)

    def run(self):
        while True:
            user = input(" Type 1 if u already have account\n Else type 2 to register     ")
            if user == "2":
                self.email = input("Please enter your username     ")
                self.password = input("Please enter your new password   ")
                self.users.add_new_user(self.email, self.password)

                print("You have been successfully registered!")
                break
            elif user == "1":
                self.email = input("Please enter your username  ")
                self.password = input("Please neter your password   ")
                with open("user.json") as file:
                    dct = json.loads(file.read())
                logged_in = False
                for i in dct:
                    if i["name"] == self.email and i["password"] == self.password:
                        print("You have successfully logged in!")
                        logged_in = True
                        break
                else:
                    print("Either password or username is incorrect :(  please try again ")
            else:
                continue
            if logged_in:
                break

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not recognized by our system")

    def show_diaries(self):
        # if not diaries:
         with open("diaries.json") as file:
            diaries = json.loads(file.read())
            for diary in diaries:
                if diary["name"] == self.email:
                    print(diary["diary-memo"], diary["diary-tags"])

    def add_diary(self):

        memo = input('Enter a memo:      ')
        tags = input('Enter tags:        ')
        self.diarybook.new_diary(self.email, self.password, memo, tags)

        print("Your note has been added")

    def search_diaries(self):

        filter_text = input("Search for:  ")

        filtered_diaries = self.diarybook.search_diary(filter_text)
        print(filtered_diaries)

    def populate_database(self):
        diaries1 = read_from_json_into_application('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)

    def sort_diaries(self):
        sort_by = input("please type id for sorting by id, or type memo for memo    ")

        if sort_by == "memo":
            with open("diaries.json") as file:
                diaries = json.loads(file.read())
                new=[]
                for i in diaries:
                    if i['name'] == self.email:
                        new.append(i)

                for diary in sorted(new, key=lambda diary: diary["diary-memo"]):
                    print(diary)
        elif sort_by == "id":
            with open("diaries.json") as file:
                diaries = json.loads(file.read())
                new = []
                for i in diaries:
                    if i['name'] == self.email:
                        new.append(i)

                for diary in sorted(new, key=lambda diary: diary["diary-id"]):
                    print(diary)

    def quit(self):

        print("Thank you for using diarybook today")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
