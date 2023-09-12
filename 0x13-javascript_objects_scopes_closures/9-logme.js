#!/usr/bin/node

exports.logMe = (function () {
  let timesPrinted = 0;

  return function (item) {
    console.log(`${timesPrinted}: ${item}`);
    timesPrinted++;
  };
})();
