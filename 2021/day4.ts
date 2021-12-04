import { readLineByLine } from "./readFile";

function checkRows(board: string[][]) {
  return board
    .map((row) => row.every((square) => square === "-1"))
    .includes(true);
}

function checkColumns(board: string[][]) {
  for (let i = 0; i < board.length; i++) {
    if (!board.map((b) => b[i] === "-1").includes(false)) {
      return true;
    }
  }
  return false;
}

function checkBoard(board: string[][]) {
  return checkRows(board) || checkColumns(board);
}

function sumBoard(board: string[][]) {
  const summedRows = board.map(
    (row) =>
      row
        .map((square) => (Number(square) >= 0 ? Number(square) : 0))
        .reduce((prev, cur) => prev + cur),
    0
  );
  return summedRows.reduce((prev, cur) => prev + cur);
}

async function getInputs() {
  const lines = await readLineByLine("input/day4.txt");
  const numbers = lines[0].split(",");
  const boards: string[][][] = [];
  lines
    .splice(1)
    .map((l) => l.trim().split(/\s+/))
    .map((_, index, array) => {
      if (index % 5 === 0) {
        boards.push(array.slice(index, index + 5));
      }
    });
  return { numbers, boards };
}

async function part1() {
  let { numbers, boards } = await getInputs();
  let solvedBoards = 0;
  const numberOfBoards = boards.length;
  for (let i = 0; i < numbers.length; i++) {
    const numberCalled = numbers[i];
    boards = boards
      .map((board) => {
        board.map((row) =>
          row.map((square, index, arr) =>
            square === numberCalled
              ? (arr[index] = "-1")
              : (arr[index] = arr[index])
          )
        );
        if (checkBoard(board)) {
          solvedBoards += 1;
          if (solvedBoards === 1) {
            console.dir("part 1");
            console.dir({
              sum: sumBoard(board),
              numberCalled,
              total: Number(numberCalled) * sumBoard(board),
            });
          }
          if (solvedBoards === numberOfBoards) {
            console.dir("part 2");
            console.dir({
              sum: sumBoard(board),
              numberCalled,
              total: Number(numberCalled) * sumBoard(board),
            });
          }
          return null;
        }
        return board;
      })
      .filter((board) => board !== null);
  }
}

part1();
