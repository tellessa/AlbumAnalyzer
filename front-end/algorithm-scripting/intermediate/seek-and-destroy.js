function destroyer(arr) {
  let newArr;
  let valuesToRemove = [];

  // get the values to remove from the arguments
  for (const key in arguments) {
    if (key > 0) {
    console.log(`${key}: ${arguments[key]}`);
    valuesToRemove.push(arguments[key])
  }
  };
  console.log(`\nvaluesToRemove: ${valuesToRemove}`);
  // Use indexOf on our list to filter to only those values that are not in valuesToRemove
  newArr = arr.filter(element => valuesToRemove.indexOf(element) === -1)
  console.log(newArr)
  return newArr;
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3);
