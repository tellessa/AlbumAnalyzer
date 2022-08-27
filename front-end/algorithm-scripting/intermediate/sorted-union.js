function uniteUnique(arr) {
    let newArr = [];
    // no matter what you're only returning one array
    // iterate through each of the list parameters and add each
    // element to the new list, unless it's already there.
    // Work with an unknown number of arguments (up to 4)
    console.log(arguments);
    console.log(arguments.length);
    let currentArr;
    let currentItem;
    for (let i = 0; i < arguments.length; i++) {
      currentArr = arguments[i];
      for (let j = 0; j < currentArr.length; j++) {
        currentItem = currentArr[j];
        if (newArr.indexOf(currentItem) === -1) {
            newArr.push(currentItem);
        }
      }
    }
    return newArr;
  }

  let answer = uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);
  console.log(answer);
