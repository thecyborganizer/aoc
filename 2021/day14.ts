import { map } from "lodash";
import { readLineByLine } from "./readFile";

async function part1() {
  const lines = await readLineByLine("input/day14.txt");
  let polymer = lines.shift().split("");
  let rules = {};
  lines
    .filter((line) => line.includes("-"))
    .map((line) => {
      const splits = line.split(" -> ");
      rules[splits[0]] = splits[1];
    });
  for (let count = 0; count < 10; count++) {
    const nextPolymer = [];
    nextPolymer.push(polymer[0]);
    for (let index = 0; index < polymer.length - 1; index++) {
      const ruleLookup = rules[polymer.slice(index, index + 2).join("")];
      if (ruleLookup != null) {
        nextPolymer.push(ruleLookup);
      }
      nextPolymer.push(polymer[index + 1]);
    }
    polymer = nextPolymer;
  }
  let counts = {};
  polymer.map((c) => {
    if (counts[c] != null) {
      counts[c] = counts[c] + 1;
    } else {
      counts[c] = 1;
    }
  });
  const maxElement = Object.entries(counts).reduce(
    (prev: [string, number], cur: [string, number]) => {
      if (cur[1] > prev[1]) {
        return cur;
      }
      return prev;
    },
    ["zzz", -1]
  );
  const minElement = Object.entries(counts).reduce(
    (prev: [string, number], cur: [string, number]) => {
      if (cur[1] < prev[1]) {
        return cur;
      }
      return prev;
    },
    ["zzz", Number.MAX_SAFE_INTEGER]
  );
  console.dir(maxElement);
  console.dir(minElement);
  console.dir((maxElement[1] as number) - (minElement[1] as number));
}

function letterCounts(s: string) {
  let counts = {};
  s.split("").map((c) => {
    if (counts[c] != null) {
      counts[c] = counts[c] + 1;
    } else {
      counts[c] = 1;
    }
  });
  return counts;
}

async function part2() {
  const lines = await readLineByLine("input/day14.txt");
  let polymer = lines.shift().split("");
  const [first, last] = [polymer[0], polymer[polymer.length - 1]];
  let rules = {};
  lines
    .filter((line) => line.includes("-"))
    .map((line) => {
      const splits = line.split(" -> ");
      rules[splits[0]] = splits[1];
    });
  let transformations = {};
  Object.entries(rules).map(([source, toAdd]) => {
    const [char1, char2] = source.split("");
    const outputs = [[char1, toAdd].join(""), [toAdd, char2].join("")];
    transformations[source] = outputs.filter((o) =>
      Object.keys(rules).includes(o)
    );
  });
  let counts = {};
  for (let i = 0; i < polymer.length - 1; i++) {
    const sub = `${polymer[i]}${polymer[i + 1]}`;
    if (counts[sub] == null) {
      counts[sub] = 1;
    } else {
      counts[sub] = counts[sub] + 1;
    }
  }
  for (let gen = 0; gen < 40; gen++) {
    let nextCounts = {};
    Object.entries(counts).map(([pair, count]) => {
      const newEntries = transformations[pair];
      newEntries.map((e) => {
        if (nextCounts[e] == null) {
          nextCounts[e] = count;
        } else {
          nextCounts[e] = nextCounts[e] + count;
        }
      });
    });
    counts = nextCounts;
  }

  let letterCounts = {};
  Object.entries(counts).map(([letters, val]) => {
    letters.split("").map((letter) => {
      if (letterCounts[letter] != null) {
        letterCounts[letter] = letterCounts[letter] + val;
      } else {
        letterCounts[letter] = val;
      }
    });
  });
  Object.entries(letterCounts).map(([letter, val]: [string, number]) => {
    if (letter == first || letter == last) {
      letterCounts[letter] = (val + 1) / 2;
    } else {
      letterCounts[letter] = val / 2;
    }
  });
  const maxElement = Object.entries(letterCounts).reduce(
    (prev: [string, number], cur: [string, number]) => {
      if (cur[1] > prev[1]) {
        return cur;
      }
      return prev;
    },
    ["zzz", -1]
  );
  const minElement = Object.entries(letterCounts).reduce(
    (prev: [string, number], cur: [string, number]) => {
      if (cur[1] < prev[1]) {
        return cur;
      }
      return prev;
    },
    ["zzz", Number.MAX_SAFE_INTEGER]
  );
  console.dir(maxElement);
  console.dir(minElement);
  console.dir((maxElement[1] as number) - (minElement[1] as number));
}
//part1();
part2();
console.dir(letterCounts("NBCCNBBBCBHCB"));
