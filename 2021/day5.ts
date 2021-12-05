import { readLineByLine } from "./readFile";
import * as _ from "lodash";
import { group } from "console";

const GRID_SIZE = 1000;

async function part1() {
  const lines = await readLineByLine("input/day5.txt").then((lines) =>
    lines.map((l) =>
      l.split(" -> ").flatMap((p) => p.split(",").map((n) => Number(n)))
    )
  );
  const board: number[][] = Array(GRID_SIZE)
    .fill(0)
    .map(() => new Array(GRID_SIZE).fill(0));
  lines.map((l) => {
    const [x1, y1, x2, y2] = l;
    if (y1 === y2) {
      _.range(Math.min(x1, x2), Math.max(x1, x2) + 1, 1).forEach((index) => {
        board[y1][index] = board[y1][index] + 1;
      });
    }
    if (x1 === x2) {
      _.range(Math.min(y1, y2), Math.max(y1, y2) + 1, 1).forEach((index) => {
        board[index][x1] = board[index][x1] + 1;
      });
    }
    if (Math.abs(x1 - x2) === Math.abs(y1 - y2)) {
      let xrange: number[] = [];
      let yrange: number[] = [];
      if ((x1 < x2 && y1 < y2) || (x1 > x2 && y1 > y2)) {
        xrange = _.range(Math.min(x1, x2), Math.max(x1, x2) + 1);
        yrange = _.range(Math.min(y1, y2), Math.max(y1, y2) + 1);
      } else {
        xrange = _.range(Math.min(x1, x2), Math.max(x1, x2) + 1);
        yrange = _.range(Math.max(y1, y2), Math.min(y1, y2) - 1, -1);
      }
      for (let i = 0; i < xrange.length; i++) {
        board[yrange[i]][xrange[i]] = board[yrange[i]][xrange[i]] + 1;
      }
    }
  });
  /*console.log(
    board
      .map((row) => row.map((s) => (s === 0 ? "." : `${s}`)).join(""))
      .join("\n")
  );*/
  console.dir(
    board
      .map((row) => row.filter((s) => s >= 2).length)
      .reduce((prev, cur) => prev + cur)
  );
}
part1();
