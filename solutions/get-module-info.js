var request = require('request');
let cheerio = require('cheerio');

function getModuleInfo(moduleName, callback) {
  var url = 'https://www.npmjs.com/package/' + moduleName;
  request.get(url, function(err, response, html) {
    if (err) {
      callback(err);
      return;
    }
    var poop = cheerio.load(html);

    var author = poop('.last-publisher a span').text();
    var timeLastPublished = poop('.last-publisher > span').text().trim();
    var info = {
      author: author,
      timeLastPublished: timeLastPublished
    };
    callback(null, info);
  });

}

module.exports = getModuleInfo;
