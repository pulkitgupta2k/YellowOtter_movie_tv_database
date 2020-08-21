require("dotenv").config();
const express = require("express");
const cors = require("cors");
const path = require("path");
const graphqlPlayground = require("graphql-playground-middleware-express")
  .default;
const { ApolloServer } = require("apollo-server-express");
const { createServer } = require("http");
const { readFileSync } = require("fs");
const resolvers = require("./app/resolvers");
const context = require("./app/context");
const db = require("./app/database");
const typeDefs = readFileSync(
  path.resolve("./app/typedef/schema.graphql"),
  "utf-8"
);

const PORT = process.env.PORT || 3000;

var app = express();
var httpServer = createServer(app);

db.connectToDB()
  .then(() => {
    const server = new ApolloServer({
      typeDefs,
      resolvers,
      context,
    });
    server.applyMiddleware({ app });

    app.get("/", (req, res) => res.send("Welcome to Graphql Server"));
    app.get("/playground", graphqlPlayground({ endpoint: "/graphql" }));

    httpServer.timeout = 5000;
    httpServer.listen({ port: PORT }, () => {
      console.log(
        `🚀 Server Running on Port:${PORT} in ${process.env.NODE_ENV}`
      );
    });
  })
  .catch((err) => console.log("Failed to Connect"));
