import xml.etree.ElementTree as ET

input = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(input)
# findall을 이용해 users아래에 있는 user태그를 불러옴
lst = stuff.findall("users/user")
# 그럼 len(lst)는 2개의 수를 얻게 됨
print("User count:", len(lst))

for item in lst:
    print("Name", item.find("name").text)
    print("Id", item.find("id").text)
    print("Attribute", item.get("x"))
