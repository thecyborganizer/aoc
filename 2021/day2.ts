import { readLineByLine } from "./readFile";

async function part1() {
  let { depth, distance } = { depth: 0, distance: 0 };
  const lines = await readLineByLine("day2.txt").then((lines) =>
    lines.map((line) => {
      const [command, valueStr] = line.split(" ");
      const value = Number(valueStr);
      switch (command) {
        case "forward":
          distance = distance + value;
          break;
        case "down":
          depth = depth + value;
          break;
        case "up":
          depth = depth - value;
          break;
      }
    })
  );
  console.dir({ depth, distance, total: depth * distance });
}

async function part2() {
  let { aim, depth, distance } = { aim: 0, depth: 0, distance: 0 };
  const lines = await readLineByLine("day2.txt").then((lines) =>
    lines.map((line) => {
      const [command, valueStr] = line.split(" ");
      const value = Number(valueStr);
      switch (command) {
        case "down":
          aim = aim + value;
          break;
        case "up":
          aim = aim - value;
          break;
        case "forward":
          distance = distance + value;
          depth = depth + aim * value;
          break;
      }
    })
  );
  console.dir({ depth, distance, total: depth * distance });
}

part1();
part2();
