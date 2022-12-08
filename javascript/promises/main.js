const promise1 = Promise.resolve(1);
const promise2 = 2;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, "promise 3");
});
const promise4 = new Promise((resolve, reject) => {
  setTimeout(resolve, 50, "promise 4");
});

const promises = [promise1, promise2, promise3, promise4];

/* console.log('Promise All')
Promise.all(promises).then((values) => {
  console.log(values);
}); */

console.log("Promise All Settled");
Promise.allSettled(promises).then((results) =>
  results.forEach((result) => console.log(result.status, result.value))
);
// expected output: Array [3, 42, "foo"]
