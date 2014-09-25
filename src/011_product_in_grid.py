from operator import mul

def getDiagonalProd(grid, row, col, n):
    prod = 1
    
    for i in range(0, n):
        prod *= grid[row + i][col + i]

    return prod

def findGreatestProduct(grid):
    maxProd = 0

    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            # West/Left
            if c - 4 >= 0:
                prod = reduce(mul, grid[r][(c - 4):c])
                if prod > maxProd:
                    maxProd = prod
            # East/Right
            if c + 4 < len(grid[r]):
                prod = reduce(mul, grid[r][c:(c + 4)])
                if prod > maxProd:
                    maxProd = prod
            # North/Up
            if r - 4 >= 0:
                prod = reduce(mul, map(lambda x: x[c], grid[(r - 4):r]))
                if prod > maxProd:
                    maxProd = prod
            # South/Down
            if r + 4 < len(grid):
                prod = reduce(mul, map(lambda x: x[c], grid[r:(r + 4)]))
                if prod > maxProd:
                    maxProd = prod
            # North-west
            if c - 4 >= 0 and r - 4 >= 0:
                prod = 1
                for i in range(0, 4):
                    prod *= grid[r - i][c - i]
                if prod > maxProd:
                    maxProd = prod
            # North-east
            if c + 4 < len(grid[r]) and r - 4 >= 0:
                prod = 1
                for i in range(0, 4):
                    prod *= grid[r - i][c + i]
                if prod > maxProd:
                    maxProd = prod
            # South-east
            if c + 4 < len(grid[r]) and r + 4 < len(grid):
                prod = 1
                for i in range(0, 4):
                    prod *= grid[r + i][c + i]
                if prod > maxProd:
                    maxProd = prod
            # South-west
            if c - 4 >= 0 and r + 4 < len(grid):
                prod = 1
                for i in range(0, 4):
                    prod *= grid[r + i][c - i]
                if prod > maxProd:
                    maxProd = prod

    return maxProd

def readGridFile(gridFile):
    grid = []

    with open(gridFile, 'rb') as inp:
        lines = inp.readlines()
        for line in lines:
            grid.append(map(lambda x: int(x), line.strip().split()))

    return grid

if __name__ == '__main__':
    grid = readGridFile('../data/011_grid.txt')
    print findGreatestProduct(grid)
