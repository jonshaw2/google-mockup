var thumbnails = require('./create-thumbnails');

thumbnails.createThumbnails('images', function(err) {
  if (err) {
    console.log(err.message);
    return;
  }
  console.log('It worked');
});
