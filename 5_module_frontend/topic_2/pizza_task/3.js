function getSum(sum = 0) {
  function inner_func(num) {
    if (num === undefined) {
      return sum;
    } else {
      sum = sum + num;
      return inner_func;
    }
  }

  return inner_func;
}

result = getSum(1)(2)(3)();
console.log(result);
