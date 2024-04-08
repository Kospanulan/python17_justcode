// function get_n_numbers(n) {
//   for (i = n; i > 0; i--) {
//     console.log(i);
//   }
// }

function get_n_numbers(n) {
  if (n == 0) {
    return;
  }

  console.log(n);
  return get_n_numbers(n - 1);
}

get_n_numbers(4);
