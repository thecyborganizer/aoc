import { readLineByLine } from "./readFile";

async function part1() {
  const positions = await readLineByLine("input/day7.txt").then((line) =>
    line[0].split(",").map((n) => Number(n))
  );
  let minFuelCost = Number.MAX_SAFE_INTEGER;
  let minPos = Number.MAX_SAFE_INTEGER;
  positions.map((pos, _, arr) => {
    const fuelCost = arr.reduce((prev, cur) => prev + Math.abs(cur - pos), 0);
    if (fuelCost < minFuelCost) {
      minFuelCost = fuelCost;
      minPos = pos;
    }
  });
  console.dir({ minFuelCost, minPos });
}

function calculateCost(start: number, end: number) {
  const n = Math.abs(start - end);
  return (n * (n + 1)) / 2;
}

async function part2() {
  const positions = await readLineByLine("input/day7.txt").then((line) =>
    line[0].split(",").map((n) => Number(n))
  );
  let minFuelCost = Number.MAX_SAFE_INTEGER;
  let minPos = Number.MAX_SAFE_INTEGER;
  positions.map((pos, _, arr) => {
    const fuelCost = arr.reduce(
      (prev, cur) => prev + calculateCost(cur, pos),
      0
    );
    if (fuelCost < minFuelCost) {
      minFuelCost = fuelCost;
      minPos = pos;
    }
  });
  console.dir({ minFuelCost, minPos });
}

part1();
part2();
