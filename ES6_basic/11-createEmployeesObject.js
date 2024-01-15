export default function createEmployeesObject(departmentName, employees) {
  const result = {};
  result[departmentName] = employees;
  return result;
}
