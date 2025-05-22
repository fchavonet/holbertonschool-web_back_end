import express from "express";

import {
    listProducts,
    getItemById,
    reserveStockById,
    getCurrentReservedStockById
} from "./9-stock.js";

const app = express();
const port = 1245;

// GET /list_products.
app.get("/list_products", (request, result) => {
    const formatted = [];

    for (const product of listProducts) {
        formatted.push({
            itemId: product.id,
            itemName: product.name,
            price: product.price,
            initialAvailableQuantity: product.stock
        });
    }

    result.json(formatted);
});

// GET /list_products/:itemId.
app.get("/list_products/:itemId", async (request, result) => {
    const id = parseInt(request.params.itemId, 10);
    const product = getItemById(id);

    if (!product) {
        result.json({ status: "Product not found" });
    } else {
        const reserved = await getCurrentReservedStockById(id);
        let currentQuantity;

        if (typeof reserved === "number") {
            currentQuantity = product.stock - reserved;
        } else {
            currentQuantity = product.stock;
        }

        result.json({
            itemId: product.id,
            itemName: product.name,
            price: product.price,
            initialAvailableQuantity: product.stock,
            currentQuantity: currentQuantity
        });
    }
});

// GET /reserve_product/:itemId.
app.get("/reserve_product/:itemId", async (request, result) => {
    const id = parseInt(request.params.itemId, 10);
    const product = getItemById(id);

    if (!product) {
        result.json({ status: "Product not found" });
    } else {
        const reserved = await getCurrentReservedStockById(id);
        const available = product.stock - reserved;

        if (available < 1) {
            result.json({ status: "Not enough stock available", itemId: id });
        } else {
            await reserveStockById(id, reserved + 1);
            result.json({ status: "Reservation confirmed", itemId: id });
        }
    }
});

// Start server.
app.listen(port, () => {
    console.log("API available on localhost port " + port);
});
