function frankenSplice(arr1, arr2, n) {
  let arr3 = [].concat(arr2);
  arr3.splice(n, 0, ...arr1)
  console.log(arr3);
  return arr3;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2);
