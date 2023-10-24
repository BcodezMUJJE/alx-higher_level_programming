#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 101-starwars_characters.js <Movie ID>');
  process.exit(1);
}
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characterUrls = filmData.characters;

      const fetchCharacter = (url) => {
        request(url, (characterError, characterResponse, characterBody) => {
          if (!characterError && characterResponse.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
            // Fetch the next character if available
            const nextCharacterUrl = characterUrls.shift();
            if (nextCharacterUrl) {
              fetchCharacter(nextCharacterUrl);
            }
          } else {
            console.error(characterError);
          }
        });
      };
      // Start fetching characters
      if (characterUrls.length > 0) {
        fetchCharacter(characterUrls.shift());
      }
    } else {
      console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    }
  }
});

