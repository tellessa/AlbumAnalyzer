function filteredArray(arr, elem) {
    let newArr = [];
    // Only change code below this line
    // remove the entire array if it contains elem
    for (let i = 0; i < arr.length; i++) {
      console.log(`elem: ${elem}`)
      console.log(`arr[i]: ${arr[i]}`)
      console.log(`arr[i].indexOf(elem): ${arr[i].indexOf(elem)}`)
      if (arr[i].indexOf(elem) === -1) {
        console.log(`adding ${arr[i]} to newArr`)
        newArr.push(arr[i])
      }
    }
    // Only change code above this line
    return newArr;
  }

  console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3));
  console.log();
  console.log(filteredArray([["amy", "beth", "sam"], ["dave", "sean", "peter"]], "peter"));