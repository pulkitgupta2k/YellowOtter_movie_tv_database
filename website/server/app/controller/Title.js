const mongoose = require("mongoose");
const { Master } = require("../model/Title");

const findById = (id) =>
  Master.findOne({ id })
    .populate({
      path: "cast",
      populate: {
        path: "cast_id",
        model: Cast,
      },
    })
    .populate({
      path: "episode",
      populate: "episode",
    })
    .exec()
    .then((res) => res.toJSON())
    .catch((err) => {
      console.log(err);
      return new Error(err);
    });
module.exports = {
  findById,
};
