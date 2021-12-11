import { readLineByLine } from "./readFile";

const openers = ["<", "{", "[", "("];
const closers = [">", "}", "]", ")"];
const scores = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137,
};

const part2scores = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4,
};

async function part1() {
  const lines = await readLineByLine("input/day10.txt").then((lines) =>
    lines.map((line) => line.split(""))
  );
  const lineScores = lines.map((line) => {
    const parsed = [];
    let score = 0;
    line.map((c) => {
      if (score != 0) {
        return;
      }
      const index = openers.findIndex((o) => o === c);
      if (index >= 0) {
        parsed.push(closers[index]);
      } else {
        const closer = parsed.pop();
        if (closer !== c) {
          score = score + scores[c];
        }
      }
    });
    return score;
  });
  console.dir(lineScores.reduce((prev, cur) => prev + cur));
}

async function part2() {
  const lines = await readLineByLine("input/day10.txt").then((lines) =>
    lines.map((line) => line.split(""))
  );
  const filteredLines = lines
    .map((line) => {
      const parsed = [];
      let score = 0;
      line.map((c) => {
        if (score != 0) {
          return;
        }
        const index = openers.findIndex((o) => o === c);
        if (index >= 0) {
          parsed.push(closers[index]);
        } else {
          const closer = parsed.pop();
          if (closer !== c) {
            score = score + scores[c];
          }
        }
      });
      return score === 0 ? line : null;
    })
    .filter((l) => l !== null);
  const completions = filteredLines.map((line) => {
    const require: string[] = [];
    line.map((c) => {
      const index = openers.findIndex((o) => o === c);
      if (index >= 0) {
        require.push(closers[index]);
      } else {
        const required = require.pop();
        if (c !== required) {
          console.dir("not a valid string");
        }
      }
    });
    return require.reverse();
  });
  const completionScores = completions.map((cs) => {
    return cs.reduce((total, c) => {
      return total * 5 + part2scores[c];
    }, 0);
  });
  console.dir(
    completionScores.sort((a, b) => a - b)[(completionScores.length - 1) / 2]
  );
}

//part1();
part2();
