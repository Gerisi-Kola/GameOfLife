import json

file = "./constant_and_rule.json"

def get_constant_and_limit():
    data = open(file,"r")
    list_question = json.load(data)
    data.close()
    return list_question




if __name__ == "__main__":
    a = get_constant_and_limit()
    print(a)
