function spinalCase(str) {
  // add a dash wherever there is a transition from lower case to upper case without a space
  //  check all unique consecutive pairs of characters
  // replace spaces with dashes
  //    use replace
  // replace underscores with dashes
  //    use replace
  // lowercase all letters
  // 
  // Create a variable for the white space and underscores.
  const regex = /\s+|_+/g;

  // Replace low-upper case to low-space-uppercase
  str = str.replace(/([a-z])([A-Z])/g, "$1 $2");

  // Replace space and underscore with -
  return str.replace(regex, "-").toLowerCase();
}

// spinalCase('This Is Spinal Tap');
// spinalCase('thisIsSpinalTap');
// spinalCase('All The-small Things');
