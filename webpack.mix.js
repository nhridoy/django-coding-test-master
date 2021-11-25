let mix = require("laravel-mix");
var path = require("path");

mix
  .js("src/templates/assets/js/app.js", "js")
  .sass("src/templates/assets/scss/main.scss", "css")
  //   .vue({ version: 2 })
  //   .react("resources/js/app.jsx", "public/js/app.js")
  .setPublicPath("src/static")
  .options({
    runtimeChunkPath: "static/rr",
  });
