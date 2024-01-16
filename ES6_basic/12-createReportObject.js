export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList },
    getNumberOfDepartments: (employees) => Object.keys(employees).length,
  };
}
