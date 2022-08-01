function mutation(arr) {
  let one_that_must_contains_all = arr[0];
  let contains_lowered = one_that_must_contains_all.toLowerCase();
  let letters_to_check_for = arr[1];
  for (let i = 0; i < letters_to_check_for.length; i++) {
    let letter = letters_to_check_for[i];
    let letter_lowered = letter.toLowerCase();
    console.log(letter_lowered);
    if (contains_lowered.includes(letter_lowered)) continue;
    console.log();
    return false;
  }
  console.log();
  return true;
}

mutation(["hello", "hey"]);
