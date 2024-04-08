// const say_hi = () => 5;

// const say_hi = () => {
//     console.log("Hello World 3")
//     return 5
// };

function get_sum(a, b, my_func) {
  return my_func(a) + my_func(b);
}

console.log(
  "result:",
  get_sum(1, 7, (x) => x * x)
);
