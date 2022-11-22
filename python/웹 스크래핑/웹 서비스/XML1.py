import xml.etree.ElementTree as ET

data = """
<person>
    <name>Chuck</name>
    <phone type="intl">
    010-2377-4624
    </phone>
    <email hide="yes"/>
</person>"""

# 문자열을 읽고
tree = ET.fromstring(data)
# tree.find("name")은 name이라는 태그를 찾는것
# .text는 문자 정보(Chuck)를 받는 것
print("Name:", tree.find("name").text)
# get("hide")는 hide라는 속성의 내용을 요청
print("Attr:", tree.find("email").get("hide"))
