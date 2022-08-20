// function largestOfFour(arr) {
//     let sub_arr;
//     console.log(arr[0]);
//     // console.log(arr[1]);
//     // console.log(arr[2]);
//     // console.log(arr[3]);
//     for (let i; i < arr.length; i++) {
//       sub_arr = arr[i];
//     //   console.log(sub_arr);
//     }
//     // console.log(arr);
//     return arr;
//   }
function largestOfFour(arr) {
    const results = [];
    for (let i = 0; i < arr.length; i++) {
      let largestNumber = arr[i][0];
      for (let j = 1; j < arr[i].length; j++) {
        if (arr[i][j] > largestNumber) {
          largestNumber = arr[i][j];
        }
      }
      results[i] = largestNumber;
    }

    return results;
  }

//   largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
  console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));