from openpyxl import load_workbook

wb = load_workbook("test.xlsx")
ws = wb.active

for x in range(1, ws.max_row+1):
    for y in range(1, ws.max_column+1):
        print(ws.cell(row=x, column=y).value, end=" ")

ws = wb["test2"]

print()
print("---------------------------------------------------------")

# test2 시트의 전체 데이터 소환
for row in ws.iter_rows(min_row=3, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
    for cell in row:
        print(cell.value, end="\t")
    print("")

print()
print("---------------------------------------------------------")

# 영어 점수가 90점 이상인 사람의 번호 추출
for row in ws.iter_rows(min_row=4, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
    if int(row[2].value) >= 90:
        print(f'{row[0].value}번 학생은 영어 90점 이상')

# ws.insert_rows(8, 5) #8번째 행에 5줄을 추가
# ws.delete_rows(8, 3) #8번쨰 행부터 3줄을 삭제
# ws.delete_cols(2) #B열을 삭제

print()
print("---------------------------------------------------------")

# 값 찾아 바꾸기
for row in ws.iter_rows(max_row=4):
    for cell in row:
        if cell.value == "영어":
            cell.value = "컴퓨터"
            print(cell, "변경 완료")

# 데이터 이동
ws.move_range("B3:C53", rows=0, cols=1)


wb.save("test.xlsx")
