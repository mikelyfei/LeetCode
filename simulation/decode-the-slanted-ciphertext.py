class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        board = [[0] * cols for _ in range(rows)] 
        n_letters = 0
        for i in range(rows):
            for j in range(cols):
                board[i][j] = encodedText[i*cols + j]
                if encodedText[i*cols + j].isalpha():
                    n_letters += 1
        res = []
      
        for j in range(cols):
            for i in range(rows):
                if i+j < cols and n_letters > 0:
                    res.append(board[i][j+i])
                    if board[i][j+i].isalpha():
                        n_letters -= 1
        return "".join(res)