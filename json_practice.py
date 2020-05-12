import json

class PracticeJson:
    def __init__(self):
        self.data = {"a":1, "b":2}

    def practice_dump(self):
        with open("./demo.json","w") as fs:
            json.dump(self.data, fp=fs)

    def practice_dumps(self):
        print(self.data)
        print(type(self.data))
        print(type(json.dumps(self.data)))
        print(json.dumps(self.data))

    def practice_load(self):
        print(type(json.load(open("./demo.json", "r"))))
        print(json.load(open("./demo.json", "r")))

    def practice_loads(self):
        json_data = json.dumps(self.data)
        print(type(json_data))
        print(json.loads(json_data))
        print(type(json.loads(json_data)))

practice_json = PracticeJson()
practice_json.practice_load()