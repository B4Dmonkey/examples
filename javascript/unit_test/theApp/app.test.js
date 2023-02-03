
const the_app = "The App";

const the_features = () => {
  test("The test should pass", () => {
    expect(true).toBe(true);
  });

  test("The test should only contain primitives", () => {
    expect(true).toBe(true);
  });

  test("Unless officially mocked", () => {

  });
};
describe(the_app, the_features);
