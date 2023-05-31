import { useAuthService } from "./index.js";
const { defineEndPoint } = useAuthService;

export const phoneStatus = defineEndPoint("phoneStatus", {
  get: () => {},
});
