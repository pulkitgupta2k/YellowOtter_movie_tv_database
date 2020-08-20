const mongoose = require("mongoose");

const { Schema, model } = mongoose;

const CastSchema = new Schema(
  {
    _id: {
      type: String,
    },
  },
  { strict: false }
);
const Cast = model("Cast", CastSchema);

const EpisodeSchema = new Schema(
  {
    _id: { type: String },
  },
  { strict: false }
);
const Episode = model("Episode", EpisodeSchema);

const ProviderSchema = new Schema({ _id: { type: String } }, { strict: false });
const Provider = model("Provider", ProviderSchema);

const MasterSchema = new Schema(
  {
    _id: {
      type: String,
    },
    cast: [
      {
        cast_id: {
          type: String,
          ref: Cast,
        },
      },
    ],
    episode: [
      {
        type: String,
        ref: Episode,
      },
    ],
    provider_data: [
      {
        _id: {
          type: String,
          ref: Provider,
        },
      },
    ],
  },
  { strict: false }
);

const Master = model("Master", MasterSchema);
module.exports = {
  Master,
  Cast,
  Episode,
  Provider,
};
