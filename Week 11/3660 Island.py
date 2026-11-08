"""Island"""

def bfs(start_r, start_c, grid, rows, cols):
    """Explore island using standard list BFS."""
    queue = [(start_r, start_c)]
    grid[start_r][start_c] = 0
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    head = 0
    while head < len(queue):
        r, c = queue[head]
        head += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc))


def main():
    """Main execution function."""
    first_line = input().split()
    if not first_line:
        return
    m = int(first_line[0])
    n = int(first_line[1])

    grid = []
    for _ in range(m):
        row = [int(x) for x in input().split()]
        grid.append(row)
    island_count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                island_count += 1
                bfs(r, c, grid, m, n)
    print(island_count)
if __name__ == "__main__":
    main()
