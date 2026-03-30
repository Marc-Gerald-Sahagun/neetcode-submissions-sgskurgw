class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for __ in range(9)]
        cols = [set() for __ in range(9)]
        boxes = {}

        for i in range(9): # rows
            for j in range(9): # columns
                num = board[i][j]

                if num == ".":
                    continue

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)
                

                box_keys = (i // 3, j //3)
                if box_keys not in boxes:
                    boxes[box_keys] = set()
                if num in boxes[box_keys]:
                    return False
                boxes[box_keys].add(num)
        
        return True