function my_func(sum = 0) {
  function inner(value) {
    if (value !== undefined) {
      sum += value;
      return inner;
    } else {
      return sum;
    }
  }
  return inner;
}

let res1 = my_func(1)(4)(1)(6)(); // res = 12
console.log(res1);
let res2 = my_func(1)(6)(); // res = 7
console.log(res2);
