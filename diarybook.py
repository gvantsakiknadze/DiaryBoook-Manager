import datetime
from Users import User
import json


class Diary:
    last_id = 0

    def __init__(self, memo, tags=' '):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        Diary.last_id += 1

        self.id = Diary.last_id

    def match(self, filter_text):
        return filter_text in self.tags or filter_text in self.memo


class DiaryBook:
    def __init__(self):
        self.diaries = []
        # self.user = User()

    def new_diary(self, email, password, memo, tags):
        new_diary = Diary(memo, tags)
        new_user = User(email, password)
        with open("diaries.json") as file:
            self.diaries = json.loads(file.read())
        with open("diaries.json", "w") as file:
            self.diaries.append({"name" : new_user.email, "diary-memo" : new_diary.memo, "diary-tags": new_diary.tags, "diary-id" : new_diary.id})
            json.dump(self.diaries, file, indent=6)

    def search_diary(self, filter_text):
        filtered_list = []
        with open("diaries.json") as file:
            diaries = json.loads(file.read())
            for diary in diaries:
                if filter_text in diary["diary-memo"] or filter_text in diary["diary-memo"]:
                    filtered_list.append(diary)

        return filtered_list
        # filtered_list=[diary for diary in self.diaries if diary.match(filter_text)]





