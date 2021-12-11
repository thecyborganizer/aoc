import { readLineByLine } from "./readFile";

function addAndResolveFlash(row, col, grid, hasFlashed) {
  if (row < 0 || row >= 10 || col < 0 || col >= 10) {
    return;
  }
  grid[row][col] = grid[row][col] + 1;
  if (!hasFlashed[row][col] && grid[row][col] > 9) {
    hasFlashed[row][col] = true;
    addAndResolveFlash(row - 1, col, grid, hasFlashed);
    addAndResolveFlash(row + 1, col, grid, hasFlashed);
    addAndResolveFlash(row, col + 1, grid, hasFlashed);
    addAndResolveFlash(row, col - 1, grid, hasFlashed);
    addAndResolveFlash(row - 1, col - 1, grid, hasFlashed);
    addAndResolveFlash(row + 1, col + 1, grid, hasFlashed);
    addAndResolveFlash(row - 1, col + 1, grid, hasFlashed);
    addAndResolveFlash(row + 1, col - 1, grid, hasFlashed);
  }
}

async function part1() {
  let grid = await readLineByLine("input/day11.txt").then((lines) =>
    lines.map((line) => line.split("").map((n) => Number(n)))
  );
  let hasFlashed: boolean[][] = Array(10)
    .fill(false)
    .map(() => new Array(10).fill(false));

  let total = 0;
  for (let steps = 0; steps < 999; steps++) {
    for (let row = 0; row < grid.length; row++) {
      for (let col = 0; col < grid.length; col++) {
        addAndResolveFlash(row, col, grid, hasFlashed);
      }
    }
    total =
      total +
      hasFlashed
        .map((row) => row.filter((x) => x === true).length)
        .reduce((prev, cur) => prev + cur);
    if (
      hasFlashed
        .map((row) => row.every((x) => x === true))
        .every((x) => x === true)
    ) {
      console.dir({ sync: steps + 1 });
    }
    hasFlashed = hasFlashed.map((row) => row.map((i) => false));
    grid = grid.map((row) => row.map((i) => (i > 9 ? 0 : i)));
  }
  //console.log(grid.map((row) => row.map((i) => `${i}`).join("")).join("\n"));
  console.dir({ total });
}
part1();
