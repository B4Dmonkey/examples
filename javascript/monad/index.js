class MockResponse {
  constructor(fn) {
    this.resFns = fn;
  }

  withFn(fn) {
    this.resFns = [...(this.resFns || []), ...Object.values(fn())];
    return this;
  }

  build() {
    const calledFns = [];
    const res = new Proxy(
      {},
      {
        get(target, prop) {
          calledFns.push(prop);
          return new Proxy({}, this);
        },
        apply(target, thisArg, args) {
          return calledFns.reduce(
            (acc, fnName) => ({ ...acc, [fnName]: () => {} }),
            {}
          );
        },
      }
    );
    this.resFns.forEach((fn) => {
      const fnName = fn.name;
      res[fnName] = fn;
    });
    return res;
  }
}

const mockResponse = new MockResponse()
  .withFn(() => ({
    someFn: () => console.log("executing someFn"),
  }))
  .withFn(() => ({ someOtherFn: () => console.log("executing someOtherFn") }))
  .build();

  console.log(mockResponse.someFn().someOtherFn());
  console.log(mockResponse.someOtherFn().someFn());
