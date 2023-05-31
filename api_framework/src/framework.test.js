import { beforeEach, describe, it, expect } from "vitest";
import request from "supertest";
import { createServer } from "./framework.js";

describe("Framework", () => {
  let server;

  beforeEach(() => {
    server = createServer();
  });

  it("creates the server with a default route", async () => {
    const res = await request(server._app).get("/").expect(200);
  });

  it("creates a path using defineEndpoint if an http method is ", async () => {
    const { defineEndpoint } = server;
    defineEndpoint("test", {
      get: () => "The test works",
    });
    const res = await request(server._app).get("/test").expect(200);
  });

  it("creates a path using defineService if an http method is ", async () => {
    const { defineService } = server;
    defineService("test", {
      get: () => "The test works",
    });
    const res = await request(server._app).get("/test").expect(200);
  });

  it.only("creates a using defineEndpoint that is scoped to defineService", async () => {
    const { defineService } = server;
    console.log('Whats my defineEndpoint')
    const { defineEndpoint } = defineService("test-service");
    console.log('after unpacking defineEndpoint')
    console.log('defineEndpoint', defineEndpoint)
    defineEndpoint("test-endpoint", {
      get: () => "The test works",
    });

    const res = await request(server._app)
      .get("/test-service/test-endpoint")
      .expect(200);
  });
});
