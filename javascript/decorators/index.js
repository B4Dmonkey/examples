function decorator (value, context) {
  console.log("decorated value is:", value);
  console.log("context is: ", context);
}

@decorator
class C {
  @decorator // decorates a class field
  p = 5;

  @decorator // decorates a method
  m() {}

  @decorator // decorates a getter
  get x() {}

  @decorator // decorates a setter
  set x(v) {}
}

console.log(C.p)