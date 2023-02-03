/* 
  Write A function function 
    solution(a)
  that, given an array A consisting of N integers, returns the maximum sum of two
  numbers whose digits add up to an equal sum. If there are no two numbers whose digits
  have an equal sum, the function should return -1.

  Examples:
  1. Given A = [51,71,17,42], the function should return 93. There are two pairs of
  numbers whose digits add up to an equal sum: (51, 42) and (17, 71). THe first pair sums
  up to 93.

  2. Given A = [42,33,60], the function should return 102. The digits of all numbers in A
  add up to the same sum, and choosing to add 42 and 60 gives the result 102.

  3. Given A = [51, 32, 43], the function should return -1, since all  numbers in A have digits
  that add up to different, unique sums.
*/

function sumValue(value) {
  let sum = 0;
  while (value) {
    sum += value % 10;
    value = Math.floor(value / 10);
  }
  // console.log(sum);
  return sum;
}

function reduceSums(sumObj, value) {
  const key = sumValue(value);
  if (sumObj[key]) {
    sumObj[key] = sumObj[key].push(value);
    return sumObj;
  }
  sumObj[key] = [value];
  return sumObj;
}

function solution(A) {
  console.log(`Begin solution for [${A}]`);
  // console.log(`Mapping the sums ${A.map((number) => sumValue(number))}`);
  const redSum = A.reduce((sumObj, value) => reduceSums(sumObj, value), {});
  console.log(`Reducing the sums ${redSum}`);
  console.dir(redSum)

  // find the sum of all the digits and store them on a dict
  // key = sum ; value = list of all the numbers in that sum
  // filter out the values that don't have more than 2 items
  // if dict is empty return -1
  // filter out everything but the highest 2 values
  // get the sum of everything
  return A;
}

const one = [51, 71, 17, 42];
const two = [42, 33, 60];
const three = [51, 32, 43];

console.log(`Example One\nInput: ${one}\nOutput:${solution(one)}\n`);
// console.log(`Example Two\nInput: ${two}\nOutput:${solution(two)}\n`);
// console.log(`Example Three\nInput: ${three}\nOutput:${solution(three)}\n`);
