import { readLineByLine } from "./readFile";

async function part1() {
  let fish = await readLineByLine("input/day6test.txt").then((lines) =>
    lines[0].split(",").map((n) => Number(n))
  );
  for (let i = 0; i < 18; i++) {
    let toAdd = 0;
    for (let j = 0; j < fish.length; j++) {
      fish[j] = fish[j] - 1;
      if (fish[j] < 0) {
        fish[j] = 6;
        toAdd = toAdd + 1;
      }
    }
    fish = fish.concat(new Array(toAdd).fill(8));
    console.dir({ gen: i, fish: fish.length });
  }
  console.dir(fish.length);
}

async function part2() {
  let fish = await readLineByLine("input/day6.txt").then((lines) =>
    lines[0].split(",").map((n) => Number(n))
  );

  const add_a_fish_this_many_days_out = Array(9).fill(0);
  for (let i = 0; i < 9; i++) {
    add_a_fish_this_many_days_out[i] = fish.filter((f) => f === i).length;
  }
  console.dir(add_a_fish_this_many_days_out.map((f) => `${f}`).join(","));

  let total_fish = fish.length;
  for (let days = 0; days < 256; days++) {
    const new_fish = add_a_fish_this_many_days_out.shift();
    add_a_fish_this_many_days_out.push(new_fish);
    add_a_fish_this_many_days_out[6] =
      add_a_fish_this_many_days_out[6] + new_fish;
    total_fish = total_fish + new_fish;
    //    console.dir(add_a_fish_this_many_days_out.map((f) => `${f}`).join(","));
    //   console.dir({ gen: days, fish: total_fish });
  }

  console.dir(total_fish);
}

//part1();
part2();
