import os


def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print('Remove file successfully')
    else:
        print('The file does not exist')


my_file = open('data.txt', 'w')
try:
    income = []
    i = 0
    amount = int(input('จำนวนครั้งที่ต้องการกรอกข้อมูล : '))
    while True:
        i += 1
        income.append(input('รายได้ ' + str(i) + ' : '))
        if i == amount:
            break
    my_file.write(str(income))

    print('บันทึกไฟล์เรียบร้อย')
except Exception as exc:
    raise Exception('ไม่สามารถเขียนข้อมูลลงไฟล์ได้') from exc
finally:
    my_file.close()
