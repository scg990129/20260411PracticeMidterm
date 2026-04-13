# @Course: CS_121 #19990SP26C
# @author: Jacob Yeung #900494756
# @Date: 20260411

TEST_CASE = [[3,5,6,7,1],
             [2,3,4,9,4],
             [4,1,5,1,2],
             [2,8,4,7,3],
             [6,8,9,1,2]]

rows = len(TEST_CASE)
cols = len(TEST_CASE[0])
result = [[0 for _ in range(cols)] for _ in range(rows)]

if len(result) != 0 and len(result[0]) != 0:
    for i in range(rows):
        for j in range(cols):
            temp = [] #[TEST_CASE[i][j]]
            try:
                temp.append(TEST_CASE[0 if i-1 < 0 else i-1][0 if j-1 < 0 else j-1])
                temp.append(TEST_CASE[0 if i-1 < 0 else i-1][j])
                temp.append(TEST_CASE[0 if i-1 < 0 else i-1][j+1])
            except IndexError:
                pass
            try:
                temp.append(TEST_CASE[i][0 if j-1 < 0 else j-1])
                # temp.append(TEST_CASE[i][j])
                temp.append(TEST_CASE[i][j+1])
            except IndexError:
                pass
            try:
                temp.append(TEST_CASE[i+1][0 if j-1 < 0 else j-1])
                temp.append(TEST_CASE[i+1][j])
                temp.append(TEST_CASE[i+1][j+1])
            except IndexError:
                pass
            result[i][j] = max(temp)

for r in result:
    print(r)
