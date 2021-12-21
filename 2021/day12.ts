import { readLineByLine } from "./readFile";

function bfs(
  node: Record<string, string[]>,
  pathSoFar: string[],
  seen: string[],
  graph: Record<string, string[]>,
  completedPaths: string[][]
) {
  const thisNode = Object.keys(node)[0];
  const updatedPath = pathSoFar.concat([thisNode]);
  const updatedSeen =
    thisNode.toLowerCase() === thisNode ? seen.concat([thisNode]) : seen;
  const toVisit = graph[thisNode].filter((n) => !seen.includes(n));
  if (toVisit.length === 0 || updatedPath.includes("end")) {
    completedPaths.push(updatedPath);
  } else {
    toVisit.map((target) => {
      let nextNode = {};
      nextNode[target] = graph[target];
      bfs(nextNode, updatedPath, updatedSeen, graph, completedPaths);
    });
  }
}

function bfs2(
  node: Record<string, string[]>,
  pathSoFar: string[],
  seen: string[],
  graph: Record<string, string[]>,
  completedPaths: string[][],
  smallCaveToVisitTwice: string,
  doubleCaveVisits: number
) {
  const thisNode = Object.keys(node)[0];
  const updatedPath = pathSoFar.concat([thisNode]);
  let updatedDoubleCaveVisits = doubleCaveVisits;
  let updatedSeen = seen.slice();
  if (thisNode.toLowerCase() === thisNode) {
    if (thisNode === smallCaveToVisitTwice) {
      updatedDoubleCaveVisits++;
      if (updatedDoubleCaveVisits === 2) {
        updatedSeen.push(thisNode);
      }
    } else {
      updatedSeen.push(thisNode);
    }
  }

  /*console.dir({
    node: thisNode,
    path: updatedPath,
    double: smallCaveToVisitTwice,
    seen: updatedSeen,
  });*/
  const toVisit = graph[thisNode].filter((n) => !updatedSeen.includes(n));
  if (toVisit.length === 0 || updatedPath.includes("end")) {
    completedPaths.push(updatedPath);
  } else {
    toVisit.map((target) => {
      let nextNode = {};
      nextNode[target] = graph[target];
      bfs2(
        nextNode,
        updatedPath,
        updatedSeen,
        graph,
        completedPaths,
        smallCaveToVisitTwice,
        updatedDoubleCaveVisits
      );
    });
  }
}

async function part1() {
  const edges = await readLineByLine("input/day12.txt").then((lines) =>
    lines.map((line) => line.split("-"))
  );
  let graph = {};
  edges.map((edge) => {
    if (graph[edge[0]]) {
      graph[edge[0]].push(edge[1]);
    } else {
      graph[edge[0]] = [edge[1]];
    }
    if (graph[edge[1]]) {
      graph[edge[1]].push(edge[0]);
    } else {
      graph[edge[1]] = [edge[0]];
    }
  });
  const completedPaths = [];
  bfs({ start: graph["start"] }, [], [], graph, completedPaths);
  console.dir(completedPaths.filter((p) => p.includes("end")).length);
}

async function part2() {
  const edges = await readLineByLine("input/day12.txt").then((lines) =>
    lines.map((line) => line.split("-"))
  );
  let graph = {};
  edges.map((edge) => {
    if (graph[edge[0]]) {
      graph[edge[0]].push(edge[1]);
    } else {
      graph[edge[0]] = [edge[1]];
    }
    if (graph[edge[1]]) {
      graph[edge[1]].push(edge[0]);
    } else {
      graph[edge[1]] = [edge[0]];
    }
  });

  const smallCaves = Object.keys(graph).filter(
    (c) => c !== "start" && c !== "end" && c.toLowerCase() === c
  );

  console.dir(smallCaves);
  const completedPaths: string[][] = [];
  smallCaves.map((smallCaveToVisitTwice) => {
    const seen = [];
    bfs2(
      { start: graph["start"] },
      [],
      seen,
      graph,
      completedPaths,
      smallCaveToVisitTwice,
      0
    );
  });
  console.dir(
    completedPaths.filter((p) => p.includes("end")).map((p) => p.join(","))
  );
  const paths = new Set(
    completedPaths
      .filter((p) => p.includes("end"))
      .map((p) => JSON.stringify(p))
  );
  console.dir(paths.size);
}

//part1();
part2();
