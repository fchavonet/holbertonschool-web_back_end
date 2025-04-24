function calculateNumber(a, b) {
  rounded_a = Math.round(a);
  rounded_b = Math.round(b);
  return (rounded_a + rounded_b);
}

module.exports = calculateNumber;
