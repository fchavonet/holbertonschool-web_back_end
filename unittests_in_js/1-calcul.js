function calculateNumber(type, a, b) {
    rounded_a = Math.round(a);
    rounded_b = Math.round(b);

    if (typeof type !== "string") {
        return "Error";
    }

    if (type === "SUM") {
        return (rounded_a + rounded_b);
    }
    else if (type === "SUBTRACT") {
        return (rounded_a - rounded_b);
    }
    else if (type === "DIVIDE") {
        if (rounded_b === 0) {
            return "error";
        }

        return (rounded_a / rounded_b);
    }
}

module.exports = calculateNumber;
