rows={}
cols={}
boxes={}
for r in range(9):
    for c in range(9):
        value=board[r][c]
        if value==".":
            continue
        box_key=(r//3,c//3)
        rows.setdefault(r,set())
        cols.setdefault(c,set())
        boxes.setdefault(box_key.set())
        if value in rows[r] or value in cols[c] or value in boxes[box_key]:
            print(False)
            break
        rows[r].add(value)
        cols[c].add(value)
        boxes[box_key].add(value)
else:
    print(True)        