function my_func(a) {
  let sum = typeof a !== "undefined" ? a : 0;
  function innerFunc(nextNum) {
    if (arguments.length === 0) {
      return sum;
    }
    sum += nextNum;
    return innerFunc;
  }
  return innerFunc;
}

let res1 = my_func(1)(4)(1)(6)();
console.log(res1);
let res2 = my_func(1)(6)();
console.log(res2);
