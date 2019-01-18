import ls from 'localstorage-ttl';
import * as imdb from 'imdb-api';

export default async (name) => {
  const cached = ls.get(name);
  if (cached) {
    return cached;
  }
  const data = await imdb.get({name}, {apiKey: 'ce9a73ab'});
  ls.set(name, data);
  return data;
}
