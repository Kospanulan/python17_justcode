function getSum(x) {
  function wrapper(y) {
    console.log("x:", x);
    console.log("y:", y);
    return x + y;
  }

  return wrapper;
}

var res = getSum(1)(4);
console.log("result:", res);

getSum(1)(4)(6)(2)(); // res = 13
getSum(1)(4)(); // res = 5
getSum(1)(4)(6)(8)(1); // res = 20
