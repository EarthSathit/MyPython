import ast
my_file = open("data.txt", "r")
try:
    data = ast.literal_eval(my_file.read())
    total = 0
    for item in data:
        total += int(item)
    answer = "รวมทั้งหมด {} บาท"
    print(answer.format(total))
except Exception as exc:
    raise Exception("ไม่สามารถอ่านข้อมูลจากไฟล์ได้") from exc
finally:
    my_file.close()
