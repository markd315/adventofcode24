from __future__ import annotations

from copy import deepcopy
from queue import PriorityQueue

TURN_DIRECTIONS = {
    (0, -1): [(1, 0), (-1, 0)],
    (0, 1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, 1), (0, -1)],
    (1, 0): [(0, 1), (0, -1)],
}


def run(part: int, debug: bool = False):
    file_name = f"../input/16.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


class Box:
    def __init__(
        self,
        parent: Box | None = None,
        position: tuple[int, int] = (-1, -1),
        direction: tuple[int, int] = (0, 0),
    ) -> None:
        self.parent = parent
        self.position = position
        self.direction = direction

    def __eq__(self, other):
        return self.position == other.position

    def __gt__(self, other):
        return self.position < other.position

    def __hash__(self):
        return hash((self.position[0], self.position[1], self.direction))

    def __repr__(self):
        return f"({self.position[0]},{self.position[1]}) {self.direction}"


def run_maze(maze, start, end) -> tuple[list, int, int]:
    best_cost = 9999999999
    best_path: list[tuple[int, int]] = []

    start_node = Box(None, start, direction=(1, 0))
    end_node = Box(None, end)

    todo: PriorityQueue[tuple[int, Box]] = PriorityQueue()
    visited: dict[Box, int] = {}
    good_spots: set[tuple[int, int]] = set()

    todo.put((0, start_node))

    while not todo.empty():
        current_cost, current_node = todo.get()
        assert isinstance(current_node, Box)

        if current_node in visited and visited[current_node] < current_cost:
            continue

        visited[current_node] = current_cost

        # Found the end
        if current_node == end_node and current_cost <= best_cost:
            path = []
            current: Box | None = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent

            best_path = deepcopy(path)
            if best_cost != current_cost:
                good_spots = set()
                best_cost = current_cost

            good_spots.update(path)

            continue

        direction = current_node.direction
        new_node = (
            current_node.position[0] + direction[0],
            current_node.position[1] + direction[1],
        )
        if not is_inbounds(maze, new_node):
            continue
        if maze[new_node[1]][new_node[0]] != 0:
            new_box = Box(current_node, new_node, direction)
            todo.put((current_cost + 1, new_box))

        for direction in TURN_DIRECTIONS[current_node.direction]:
            new_node = (
                current_node.position[0] + direction[0],
                current_node.position[1] + direction[1],
            )

            if not is_inbounds(maze, new_node):
                continue

            # Make sure it is not a wall
            if maze[new_node[1]][new_node[0]] == 0:
                continue

            new_box = Box(current_node, new_node, direction)
            todo.put((current_cost + 1001, new_box))

    return best_path[::-1], best_cost, len(good_spots)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    show(data, debug=debug)

    start = find_in_grid(data, "S")
    end = find_in_grid(data, "E")
    grid = grid_to_int(data)

    path, results, _ = run_maze(grid, start, end)

    if debug:
        print(sorted(list(path)))

    return results


def part2(data: list[str], debug: bool = False) -> int:
    show(data, debug=debug)

    start = find_in_grid(data, "S")
    end = find_in_grid(data, "E")
    grid = grid_to_int(data)

    _, _, good_spots = run_maze(grid, start, end)

    return good_spots


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


def is_inbounds(data: list[str], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


def grid_to_int(data: list[str]) -> list[list[int]]:
    grid = []
    for row in data:
        row = row.replace("#", "0")
        row = row.replace(".", "1")
        row = row.replace("S", "1")
        row = row.replace("E", "1")
        grid.append([int(x) for x in list(row)])

    return grid


def find_in_grid(grid: list[str], character: str) -> tuple[int, int]:
    for y, row in enumerate(grid):
        try:
            x = row.index(character)
        except ValueError:
            x = -1

        if x != -1:
            return (x, y)

    return (-1, -1)


if __name__ == "__main__":
    print("Test1a: ", run(part=1,debug=True))  # 7036
    # print("Test1b: ", run(part=1, test_suffix="-test1b", debug=True))  # 11048
    # print("Real1: ", run(part=1, debug=False))  # 111480

    print("Test2a: ", run(part=2, debug=True))  # 45
    # print("Test2b: ", run(part=2, test_suffix="-test1b", debug=True))  # 64
    # print("Real2: ", run(part=2, debug=False))  # 529