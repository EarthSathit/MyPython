my_file = open("data.txt", "w")
try:
    income = []
    i = 0
    amount = input("จำนวนครั้งที่ต้องการกรอกข้อมูล : ")
    while True:
        income.append(input("รายได้ : "))
        i += 1
        if int(i) == int(amount): break
    my_file.write(str(income))

    print("บันทึกไฟล์เรียบร้อย")
except Exception as exc:
    raise Exception("ไม่สามารถเขียนข้อมูลลงไฟล์ได้") from exc
finally:
    my_file.close()
