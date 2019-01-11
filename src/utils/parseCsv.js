import parse from 'csv-parse';

export default async (input) => {
  return new Promise(((resolve, reject) => {
    parse(input, {
      columns: [false, 'show1', 'show2', 'words'],
      from_line: 2
    }, (err, output) => {
      if (err) {
        reject(err);
      } else {
        resolve(output);
      }
    })
  }))
}
