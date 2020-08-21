const title = require("../controller/Title");

const findById = async (_, { id }) => {
  const res = await title.findById(id);
  console.log(res);
  return res;
};

module.exports = {
  findById,
};
