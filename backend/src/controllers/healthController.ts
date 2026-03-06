export const healthController = (_, res) => {
  res.json({status: "ok", timestamp: new Date().toISOString()});
};
