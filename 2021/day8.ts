import { readLineByLine } from "./readFile";
import * as sets from "set-operations";

async function part1() {
  const lines = await readLineByLine("input/day8.txt").then((lines) =>
    lines.map((line) => line.split(" | ")[1].split(/\s+/))
  );

  const digitCount = lines
    .map(
      (l) =>
        l.filter(
          (word) =>
            word.length === 2 ||
            word.length === 3 ||
            word.length === 4 ||
            word.length === 7
        ).length
    )
    .reduce((prev, cur) => prev + cur);
  console.dir(digitCount);
}

async function part2() {
  const lines = await readLineByLine("input/day8.txt").then((lines) =>
    lines.map((line) => {
      const [inputs, output] = line.split(" | ");
      return {
        inputs: inputs.split(/\s+/).map((s) => s.split("")),
        output: output.split(/\s+/).map((s) => s.split("")),
      };
    })
  );
  const total = lines
    .map(({ inputs, output }) => {
      const digits: string[][] = Array(10);
      digits[1] = inputs.find((d) => d.length === 2);
      digits[7] = inputs.find((d) => d.length === 3);
      digits[4] = inputs.find((d) => d.length === 4);
      digits[8] = inputs.find((d) => d.length === 7);
      digits[6] = inputs.find(
        (d) => d.length === 6 && !sets.isSubSet(digits[1], d)
      );
      digits[9] = inputs.find(
        (d) => d.length === 6 && sets.isSubSet(digits[4], d)
      );
      digits[0] = inputs.find(
        (d) =>
          d.length === 6 &&
          !sets.isSubSet(digits[4], d) &&
          sets.isSubSet(digits[1], d)
      );
      digits[3] = inputs.find(
        (d) => d.length === 5 && sets.isSubSet(digits[1], d)
      );
      digits[5] = inputs.find(
        (d) => d.length === 5 && sets.isSubSet(d, digits[6])
      );
      digits[2] = inputs.find(
        (d) =>
          d.length === 5 &&
          !sets.isSubSet(d, digits[6]) &&
          !sets.isSubSet(digits[1], d)
      );
      //    console.dir(digits);
      const outputDigits = output.map((o) =>
        digits.findIndex((d) => sets.isSubSet(d, o) && sets.isSuperSet(d, o))
      );
      return Number(outputDigits.map((d) => `${d}`).join(""));
    })
    .reduce((prev, cur) => prev + cur);
  console.dir(total);
}

//part1();
part2();
