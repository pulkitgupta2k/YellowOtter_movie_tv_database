require("dotenv").config();
const express = require("express");
const cors = require("cors");
const path = require("path");
const grapqlPlayground = require("graphql-playground-middleware-express")
  .default;
const { ApolloServer } = require("apollo-server-express");
const { createServer } = require("http");
const { readFileSync } = require("fs");
const typeDefs = readFileSync(
  path.resolve("./app/typedef/schema.graphql"),
  "utf-8"
);
const resolvers = require("./app/resolvers");
const context = require("./app/context");
const db = require("./app/database");

db.connectToDB().then(() => {
  const app = express();
  app.use(cors);
  const httpServer = createServer(app);

  const server = new ApolloServer({
    typeDefs,
    resolvers,
    context,
  });
  server.applyMiddleware({ app });

  httpServer.timeout = 5000;
  httpServer.listen(process.env.PORT, "0.0.0.0", () => {
    console.log(
      `🚀 Server Running on Port:${process.env.PORT} in ${process.env.NODE_ENV}`
    );
  });
});
