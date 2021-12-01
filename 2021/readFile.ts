import * as fs from "fs";
import * as readline from "readline";

export async function readLineByLine(filename: string) {
  const fileStream = fs.createReadStream(filename);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  const lines: string[] = [];

  for await (const line of rl) {
    const trimmed = line.trimEnd();
    if (trimmed.length > 0) {
      lines.push(trimmed);
    }
  }

  return lines;
}
