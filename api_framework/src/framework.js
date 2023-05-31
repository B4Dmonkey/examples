import "dotenv/config";

import bodyParser from "body-parser";
import cors from "cors";
import express from "express";
import _ from "lodash";
const _app = express();

const HTTPMethodResponse = (method, request, response, next) => {
  try {
    const res = method(request, response, next);
    return response.status(200).json(res);
    // return method(request, response, next);
  } catch (error) {
    console.log(error);
    return res
      .status(500)
      .json({ error: `Internal server error. ${e.toString()}` });
  }
};

export const defineEndpoint = (path, definition = {}, root = "/") => {
  const { get, post, put, delete: del } = definition;
  const methods = { get, post, put, delete: del };
  const router = express.Router();
  const routerPath = `/${path}`;
  
  Object.keys(methods).forEach((method) => {
    if (methods[method]) {
      router[method](routerPath, (req, res, next) =>
        HTTPMethodResponse(methods[method], req, res, next)
      );
    }
  });

  Server._app.use(root, router);
};

export const defineService = (path, definition = {}) => {
  defineEndpoint(path, definition);
  const servicePath = `/${path}`;
  return { defineEndpoint: _.partialRight(defineEndpoint, servicePath) };
};

const Server = Object.freeze({
  _app,
  defineEndpoint,
  defineService,
});

export const createServer = () => {
  Server._app.use(bodyParser.json());
  Server._app.use(cors());

  Server._app.get("/", (req, res) => {
    res.status(200).send("Find the Happy Path ^_^");
  });

  return Server;
};
