import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (error) => {
	console.error("Redis client error: " + error);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
	{ id: 1, name: "Suitcase 250", price: 50, stock: 4 },
	{ id: 2, name: "Suitcase 450", price: 100, stock: 10 },
	{ id: 3, name: "Suitcase 650", price: 350, stock: 2 },
	{ id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
	const itemId = Number(id);
	for (const item of listProducts) {
		if (item.id === itemId) {
			return item;
		}
	}
	return undefined;
}

async function reserveStockById(itemId, stock) {
	await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
	const val = await getAsync(`item.${itemId}`);
	if (val === null) {
		return 0;
	} else {
		return parseInt(val, 10);
	}
}

export {
	listProducts,
	getItemById,
	reserveStockById,
	getCurrentReservedStockById,
};
