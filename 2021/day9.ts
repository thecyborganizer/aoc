import { readLineByLine } from "./readFile";

async function part1() {
  const map = await readLineByLine("input/day9.txt").then((lines) =>
    lines.map((line) => line.split("").map((n) => Number(n)))
  );
  let riskLevel = 0;
  for (let row = 0; row < map.length; row++) {
    for (let col = 0; col < map[row].length; col++) {
      const point = map[row][col];
      const isLocalMinima =
        (row === 0 || map[row - 1][col] > point) &&
        (row === map.length - 1 || map[row + 1][col] > point) &&
        (col === 0 || map[row][col - 1] > point) &&
        (col === map[row].length - 1 || map[row][col + 1] > point);
      if (isLocalMinima) {
        riskLevel = riskLevel + point + 1;
      }
    }
  }
  console.dir(riskLevel);
}

type point = {
  row: number;
  col: number;
};

function getNeighbors(map: number[][], point: point): point[] {
  const { row, col } = point;
  const neighbors = [];
  if (row !== 0) {
    neighbors.push({ row: row - 1, col });
  }
  if (row !== map.length - 1) {
    neighbors.push({ row: row + 1, col });
  }
  if (col !== 0) {
    neighbors.push({ row, col: col - 1 });
  }
  if (col !== map[row].length - 1) {
    neighbors.push({ row, col: col + 1 });
  }

  return neighbors;
}

async function part2() {
  const map = await readLineByLine("input/day9.txt").then((lines) =>
    lines.map((line) => line.split("").map((n) => Number(n)))
  );
  let localMinima = [];
  for (let row = 0; row < map.length; row++) {
    for (let col = 0; col < map[row].length; col++) {
      const point = map[row][col];
      const isLocalMinima =
        (row === 0 || map[row - 1][col] > point) &&
        (row === map.length - 1 || map[row + 1][col] > point) &&
        (col === 0 || map[row][col - 1] > point) &&
        (col === map[row].length - 1 || map[row][col + 1] > point);
      if (isLocalMinima) {
        localMinima.push({ row, col });
      }
    }
  }
  const basinSizes = localMinima.map(({ row, col }) => {
    const toVisit: point[] = [{ row, col }];
    const visited = new Set<string>();
    while (toVisit.length !== 0) {
      const visiting = toVisit.shift();
      const neighbors = getNeighbors(map, visiting);
      toVisit.push(
        ...neighbors.filter(
          (p) => !visited.has(JSON.stringify(p)) && map[p.row][p.col] !== 9
        )
      );
      visited.add(JSON.stringify(visiting));
    }
    return visited.size;
  });
  console.dir(
    basinSizes
      .sort((a, b) => b - a)
      .slice(0, 3)
      .reduce((prev, cur) => prev * cur, 1)
  );
}
//part1();
part2();
