#!/usr/bin/node
exports.esrever = function (list) {
  const swaps = Math.floor(list.length / 2);
  let j = list.length - 1;
  let tmp;

  for (let i = 0; i < swaps; i++) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    j--;
  }
  return list;
};
