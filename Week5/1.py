
def fill(x, y, grid):
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]
    if grid[y][x] == ' ':
        grid[y][x] = '.'
        for i in xrange(len(dx)):
            fill(x+dx[i], y+dy[i], grid)

x,y = map(int,raw_input('Coordinates: ').split())
grid = []
enter = raw_input('Enter: ')
while enter:
    grid.append(list(enter))
    enter = raw_input('Enter: ')

fill(x,y,grid)
for line in grid:
    print ''.join(line)