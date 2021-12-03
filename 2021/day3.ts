import { readLineByLine } from "./readFile";
import * as _ from "lodash";

function stringToInt(str: string, base: number) {
  return arrayToInt(
    str.split("").map((c) => Number(c)),
    base
  );
}

function arrayToInt(arr: number[], base: number) {
  return arr.reduce(
    (prev, cur, index, array) =>
      prev + cur * Math.pow(base, array.length - (index + 1)),
    0
  );
}

async function part1() {
  const lines = await readLineByLine("input/day3.txt");
  const gamma = [];
  for (let i = 0; i < lines[0].length; i++) {
    let [ones, zeroes] = [0, 0];
    for (let j = 0; j < lines.length; j++) {
      console.dir({ j, i, line: lines[j] });
      lines[j][i] === "1" ? (ones = ones + 1) : (zeroes = zeroes + 1);
    }
    ones > zeroes ? gamma.push(1) : gamma.push(0);
  }
  const epsilon = gamma.map((b) => (b + 1) % 2);
  console.dir(arrayToInt(gamma, 2) * arrayToInt(epsilon, 2));
}

async function part2() {
  const lines = await readLineByLine("input/day3.txt");

  let O2Candidates = lines.concat();
  let i = 0;
  for (i = 0; i < O2Candidates[0].length; i++) {
    let [ones, zeroes, match] = [0, 0, "0"];
    for (let j = 0; j < O2Candidates.length; j++) {
      O2Candidates[j][i] === "1" ? (ones = ones + 1) : (zeroes = zeroes + 1);
    }
    ones >= zeroes ? (match = "1") : (match = "0");
    _.remove(O2Candidates, (c) => c[i] !== match);
    if (O2Candidates.length === 1) {
      break;
    }
  }

  let CO2Candidates = lines.concat();
  for (i = 0; i < CO2Candidates[0].length; i++) {
    let [ones, zeroes, match] = [0, 0, "0"];
    for (let j = 0; j < CO2Candidates.length; j++) {
      CO2Candidates[j][i] === "1" ? (ones = ones + 1) : (zeroes = zeroes + 1);
    }
    ones >= zeroes ? (match = "0") : (match = "1");
    _.remove(CO2Candidates, (c) => c[i] !== match);
    if (CO2Candidates.length === 1) {
      break;
    }
  }

  console.dir({
    o2: stringToInt(O2Candidates[0], 2),
    co2: stringToInt(CO2Candidates[0], 2),
    product: stringToInt(O2Candidates[0], 2) * stringToInt(CO2Candidates[0], 2),
  });
}

//part1();
part2();
