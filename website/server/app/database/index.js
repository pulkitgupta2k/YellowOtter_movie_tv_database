const mongoose = require("mongoose");
const config = require("./config.json");
const URL = process.env.DATABASE_URL
  ? process.env.DATABASE_URL
  : "mongodb://localhost:27017/cool_db";

const connectToDB = () => {
  return mongoose
    .connect(URL, config)
    .then(() => {
      console.log("Connected To DB");
      return Promise.resolve();
    })
    .catch(() => {
      console.error(`Failed to Connect To ${URL}`);
      Promise.reject();
    });
};

module.exports = {
  connectToDB,
};