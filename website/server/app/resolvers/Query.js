const title = require("../controller/Title");

const findById = async (_, { id }) => {
  const res = await title.findById(id);
  console.log(res);
  return res;
  // return {
  //   _id: "5f34f22e8096fb18991e10fc",
  //   id: "tt4109268",
  //   name: "Asperger's Are Us",
  //   description: `In this coming of age documentary, four friends on the Autism spectrum whom have bonded through humor and performed as the comedy troupe "Asperger's Are Us" will prepare for one final, ambitious show before going their separate ways.`,
  //   genre: ["Documentary", "Comedy", "Drama"],
  //   imdb_ratings: "6.7",
  //   rt_rating: null,
  //   age_rating: "",
  //   cover_image:
  //     "https://m.media-amazon.com/images/M/MV5BMTBkZWNlNTctYjFiMy00ZDRhLThmNjYtMjkyOTljYjM1ZWUzXkEyXkFqcGdeQXVyMTU2NzQ5MzA@._V1_.jpg",
  //   air_date: "2016-11-11",
  //   trailer_link: "/video/imdb/vi870692377",
  //   cast: [
  //     ["", "Alex Lehmann", "dir", ""],
  //     [
  //       "Mark Proksch",
  //       "Self",
  //       "cast",
  //       "https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB468460248_.png",
  //     ],
  //   ],
  //   seasons: [],
  //   episode: [],
  //   title_type: "movie",
  //   __v: 0,
  // };
};

module.exports = {
  findById,
};
