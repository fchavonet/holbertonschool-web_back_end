/* eslint-disable no-plusplus */
export default function createIteratorObject(report) {
  const { allEmployees } = report;
  const flattenedEmployees = [];

  for (const department in allEmployees) {
    if (Object.prototype.hasOwnProperty.call(allEmployees, department)) {
      flattenedEmployees.push(...allEmployees[department]);
    }
  }

  let index = 0;

  return {
    next() {
      return index < flattenedEmployees.length
        ? { value: flattenedEmployees[index++], done: false }
        : { done: true };
    },
    [Symbol.iterator]() {
      return this;
    },
  };
}
