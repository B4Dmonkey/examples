const key = (key) => key
const obj = {
  a: 1,
  [key('someKey')]: 32
}

console.log('obj is', obj)

