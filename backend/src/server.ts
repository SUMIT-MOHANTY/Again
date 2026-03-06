import express from "express";
import { SERVER_PORT } from "./config";
import router from "./routes";
const app = express();
app.use(express.json());
app.use("/api", router);
app.get("/health", (_, res) => res.json({status: "ok"}));
app.listen(SERVER_PORT, () => console.log(`Server running on port ${SERVER_PORT}`));
