function getSum(n) {
  let sum = n;
  function wrapper(x) {
    if (x) {
      sum = sum + x;
      return wrapper;
    } else {
      return sum;
    }
  }
  return wrapper;
}

res = getSum(1)(4)(5)(7)(3)();
console.log(sum);
