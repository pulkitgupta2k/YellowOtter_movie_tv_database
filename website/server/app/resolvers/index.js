const Type = require("./Type");
const Query = require("./Query");
const Mutation = require("./Mutation");
const Subscription = require("./Subscription").Subscription;

module.exports = {
  Query,
  Mutation,
  Subscription,
  ...Type,
};
