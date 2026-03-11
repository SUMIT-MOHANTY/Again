import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import authRoutes from './routes/auth';
import { setupDatabase } from './db/setup';

const app = express();

app.use(helmet());
app.use(cors());
app.use(express.json());

app.use(authRoutes);

const PORT = process.env.PORT || 3000;

async function start() {
  await setupDatabase();
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}

start();

export default app;
