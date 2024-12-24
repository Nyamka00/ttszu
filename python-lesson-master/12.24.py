# import json
# x = {"name":"John", "age":30, "city":"New York"}
# y = json.loads(x)
# print(y["age"])

# x = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# x = {
#     "name"
# }

# import re
# s = 'Hello from 95020170 to about the meeting 884577466 '
# Ist = re.findall(r'\b\d{8}\b', s)
# print(Ist)

import re
s = 'Hello from ИУ02212700 to about the meeting 884577466 '
Ist = re.findall(r'\b[A-ЯӨҮ]{2}\d{8}\b', s)
print(Ist)