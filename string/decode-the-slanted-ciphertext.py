class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        board = [[0] * cols for _ in range(rows)] 
        for i in range(rows):
            for j in range(cols):
                board[i][j] = encodedText[i*cols + j]
        res = []
        for j in range(cols):
            for i in range(rows-1, 0, -1):
                if i+j < cols and board[i][0] != " ":
                    res.append(board[i][i+j])
        for j in range(cols):
            for i in range(rows):
                if i+j < cols and board[0][j] != " ":
                    res.append(board[i][j+i])
        return "".join(res)