var getModuleInfo = require('./get-module-info');

getModuleInfo('testem', function(err, info) {
  if (err) {
    console.log(err.message);
    return;
  }
  console.log(info);
});
