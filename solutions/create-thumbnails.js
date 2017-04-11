var fs = require('fs');
var gm = require('gm');
var async = require('async');

function createThumbnails(dir, callback) {

  function resizeImage(filename, resizeImageCallback) {
    gm(filename)
      .resize(240, 240)
      .write(filename, resizeImageCallback);
  }

  fs.readdir(dir, function(err, files) {
    if (err) {
      callback(err);
      return;
    }
    files = files.map(function(filename) {
      return dir + '/' + filename;
    });
    async.each(files, resizeImage, function(err) {
      if (err) {
        callback(err);
        return;
      }
      callback(null);
    });
  });

}

exports.createThumbnails = createThumbnails;
