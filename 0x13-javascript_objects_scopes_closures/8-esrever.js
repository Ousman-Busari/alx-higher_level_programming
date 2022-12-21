#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (arr, ele) {
    arr.push(ele);
    return arr;
  }, []);
};
