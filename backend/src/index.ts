import express from 'express';
import morgan from 'morgan';
import { healthRouter } from '../api/routes/health';
import { errorHandler } from '../api/middlewares/errorHandler';
import { config } from '../config/config';

const app = express();
app.use(morgan('dev'));
app.use(express.json());
app.use('/api', healthRouter);
app.use(errorHandler);

app.listen(config.PORT, () => {
  console.log(`Server running on port ${config.PORT}`);
});
