const globalArray = [5, 6, 3, 2, 9];

function nonMutatingSort(arr) {
  // Only change code below this line
  let newArr = arr.concat([]);
  console.log(newArr);
  newArr.sort(function(a, b) {
    return a - b;
  });
  return newArr;
  // Only change code above this line
}

nonMutatingSort(globalArray);
