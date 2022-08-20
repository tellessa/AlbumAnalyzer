function getIndexToIns(arr, num) {
  console.log(arr);
  if (arr == false) {
    return 0;
  };
  let sorted_arr = arr.sort(function(a, b){return a-b});
  console.log(sorted_arr);
  // console.log(arr);
  // console.log(sorted_arr);
  // assume it is less than all other array members until proven otherwise
  let insert_index = 0;
  // for 
  for (let i = 0; i < arr.length; i++) {
    insert_index = i;
    if (num <= arr[i]) {
      // it is greater than 0, 1, etc.
      console.log(`${num} <= ${arr[i]}`)
      return insert_index;
    } else {
      console.log(`${num} > ${arr[i]}`)
      // return insert_index;
    }
  }
  // increment one more time for if the element should be inserted at the end position
  insert_index++;
  console.log(insert_index);
  return insert_index;
}

// getIndexToIns([40, 60], 50);
// getIndexToIns([40, 60, 30], 50);
// getIndexToIns([5, 3, 20, 3], 5);
// getIndexToIns([], 1)
getIndexToIns([2, 5, 10], 15);
