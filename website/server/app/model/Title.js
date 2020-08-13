const mongoose = require("mongoose");
const { Schema } = mongoose;
const dataSchema = new Schema(
  { id: { type: String, unique: true } },
  { strict: false, collation: "datadumps" }
);
const Title = mongoose.model("DataDump", dataSchema, "datadumps");

module.exports = Title;
