const colors = require("tailwindcss/colors");

/** @type {import("tailwindcss").Config} */
module.exports = {
  darkMode: "media",
  content: [
    "./templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: [
          // 'system-ui',
        ],
      },
      colors: {
        // gray: {
        //   "50": "#fef3f2",
      },
    },
  },
  plugins: [
    require("flowbite/plugin"),
  ],
};

// npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
