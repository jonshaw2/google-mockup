var createThumbnails = require('./create-thumbnails-2');

createThumbnails('images', function(err) {
  if (err) {
    console.log(err.message);
    return;
  }
  console.log('It worked');
});
