import { readLineByLine } from "./readFile";

function foldGrid(grid: number[][], direction: string, val: number) {
  const newGrid = new Set<string>();
  if (direction === "y") {
    grid.map(([x, y]) => {
      if (y > val) {
        newGrid.add(JSON.stringify([x, val - (y - val)]));
      } else {
        newGrid.add(JSON.stringify([x, y]));
      }
    });
  }
  if (direction === "x") {
    grid.map(([x, y]) => {
      if (x > val) {
        newGrid.add(JSON.stringify([val - (x - val), y]));
      } else {
        newGrid.add(JSON.stringify([x, y]));
      }
    });
  }
  console.dir(newGrid);
  return Array.from(newGrid).map((x) =>
    JSON.parse(x).map((n: number) => Number(n))
  );
}

async function part1() {
  const file = await readLineByLine("input/day13.txt");
  const grid = file
    .filter((x) => x.includes(","))
    .map((line) => line.split(",").map((n) => Number(n)));
  const instructions = file
    .filter((x) => x.includes("fold"))
    .map((line) => {
      const splits = line.split("=");
      return {
        dir: splits[0].substr(splits[0].length - 1),
        val: Number(splits[1]),
      };
    });
  console.dir(grid);
  console.dir(instructions);
  console.dir(foldGrid(grid, instructions[0].dir, instructions[0].val).length);
}

async function part2() {
  const file = await readLineByLine("input/day13.txt");
  let grid = file
    .filter((x) => x.includes(","))
    .map((line) => line.split(",").map((n) => Number(n)));
  const instructions = file
    .filter((x) => x.includes("fold"))
    .map((line) => {
      const splits = line.split("=");
      return {
        dir: splits[0].substr(splits[0].length - 1),
        val: Number(splits[1]),
      };
    });
  instructions.map((i) => (grid = foldGrid(grid, i.dir, i.val)));
  const outputGrid = Array(40)
    .fill([])
    .map(() => new Array(40).fill("."));
  console.dir(grid);
  grid.map((g) => (outputGrid[g[0]][g[1]] = "#"));
  console.log(
    outputGrid.map((row) => row.map((i) => `${i}`).join("")).join("\n")
  );
}

//part1();
part2();
