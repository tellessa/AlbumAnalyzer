function chunkArrayInGroups(arr, size) {
  // last group can be as short as necessary;
  // initialize new 2D array;
  let new_arr = [];
  let chunk;
  let start;
  let end;
  // determine # elements in the array
  start = 0;
  let num_chunks = Math.ceil(arr.length / size);
  console.log(num_chunks);
  // use 'size' as the second argument to slice
  end = size;
  for (let i = 0; i < num_chunks; i++) {
  // use slice to get the new arrays
    chunk = arr.slice(start, end);
    new_arr.push(chunk);
    // console.log(arr.length);
  // add size to start & end for the next round of slice
    start += size;
    end += size;
    console.log(`start: ${start}`);
    console.log(`end: ${end}`);
  }
  // add the new arrays to the 2D array
  console.log(new_arr);
  return new_arr;
}

// chunkArrayInGroups(["a", "b", "c", "d"], 2);
// chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3)
chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3)
