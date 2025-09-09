class matrix2D:
        matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target=13
        lowRow = 0
        highRow = len(matrix) - 1
        while lowRow <= highRow:
            print(highRow,lowRow)
            midRow = lowRow + (highRow - lowRow)//2
            if matrix[midRow][0] > target:
                highRow = midRow - 1
            elif matrix[midRow][len(matrix[midRow]) - 1] < target:
                lowRow = midRow + 1
            else:
                lowCol = 0
                highCol = len(matrix[midRow]) - 1
                while lowCol <= highCol:
                    midCol = lowCol + (highCol - lowCol)//2
                    if matrix[midRow][midCol] > target:
                        highCol = midCol - 1
                    elif matrix[midRow][midCol] < target:
                        lowCol = midCol + 1
                    else:
                        break