lt=['สมชาย','สุดา','มานี','ชูใจ','แทนคุณ']
passed=0
failed=0
while True:
    intro= input("ป้อนชื่ินักเรียน: ")
    if intro =="No" or intro=="no":
        break
    if intro in lt:
        mark=float(input(f"คะแนนของ {intro}  "))
        if mark>=50:
            print(f"{intro} สอบผ่าน")
            passed+=1
        else:
            print(f"{intro} สอบไม่ผ่าน")
            failed+=1
    else:
        print("ป้อนชื่อนักเรียนไม่ถูกต้อง")
    
print("จำนวนนักเรียนที่สอบผ่าน ",passed ,"คน")
print("จำนวนนักเรียนที่ไม่สอบผ่าน",failed ,"คน")
