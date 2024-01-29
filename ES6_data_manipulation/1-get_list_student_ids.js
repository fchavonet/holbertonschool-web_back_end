export default function getListStudents(array) {
  if (!Array.isArray(array)) {
    return [];
  }

  return array.map((student) => student.id);
}
