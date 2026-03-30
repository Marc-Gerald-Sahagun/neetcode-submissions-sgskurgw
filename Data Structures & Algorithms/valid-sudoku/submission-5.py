class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for __ in range(9)]
        cols = [set() for __ in range(9)]
        boxes = {}

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                box_key = (i // 3, j // 3)
                if box_key not in boxes:
                    boxes[box_key] = set()
                
                if num in boxes[box_key]:
                    return False
                boxes[box_key].add(num)

        return True