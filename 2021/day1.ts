import { readLineByLine } from "./readFile";

async function part1() {
  const lines = await readLineByLine("day1.txt");
  console.dir(
    lines
      .map((l) => Number(l))
      .reduce((prev, cur, index, array) => {
        if (index === 0 || cur < array[index - 1]) {
          return prev;
        }
        return prev + 1;
      }, 0)
  );
}

async function part2() {
  const lines = await readLineByLine("day1.txt");
  console.dir(
    lines
      .map((l) => Number(l))
      .reduce((prev, cur, index, array) => {
        if (index <= 2) {
          return prev;
        }
        const currentWindow = cur + array[index - 1] + array[index - 2];
        const prevWindow =
          array[index - 1] + array[index - 2] + array[index - 3];
        if (currentWindow > prevWindow) {
          return prev + 1;
        }
        return prev;
      }, 0)
  );
}

part2();
