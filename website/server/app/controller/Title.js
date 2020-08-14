const mongoose = require("mongoose");
const Title = require("../model/Title");

const findById = (id) =>
  Title.findOne({ id })
    .exec()
    .then((res) => res.toJSON())
    .catch((err) => {
      console.log(err);
      return new Error(err);
    });
module.exports = {
  findById,
};
