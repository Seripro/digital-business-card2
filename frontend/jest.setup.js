require("@testing-library/jest-dom");
require("dotenv").config();
global.TextEncoder = require("util").TextEncoder;
const createMatchMedia = () =>
  function matchMedia(query) {
    return {
      matches: false,
      media: query,
      onchange: null,
      addListener: jest.fn(),
      removeListener: jest.fn(),
      addEventListener: jest.fn(),
      removeEventListener: jest.fn(),
      dispatchEvent: jest.fn(),
    };
  };

const matchMedia = createMatchMedia();
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: matchMedia,
});
Object.defineProperty(globalThis, "matchMedia", {
  writable: true,
  value: matchMedia,
});
Object.defineProperty(global, "matchMedia", {
  writable: true,
  value: matchMedia,
});
if (!global.structuredClone) {
  global.structuredClone = function structuredClone(objectToClone) {
    if (objectToClone === undefined) return undefined;
    return JSON.parse(JSON.stringify(objectToClone));
  };
}
