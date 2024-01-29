export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const filteredValues = Array.from(set).filter((value) => value.startsWith(startString));

  const cleanedValues = filteredValues.map((value) => {
    if (value.startsWith(startString)) {
      return value.replace(new RegExp(`^${startString}`), '');
    }
    return value;
  });
  return cleanedValues.join('-');
}
