#encoding "utf8"

LocationName -> Word<gram="geo">;
LocationName -> Noun<kwtype=city>;
LocationName -> Noun<kwtype=country>;

Location -> LocationName interp (Location.Name);