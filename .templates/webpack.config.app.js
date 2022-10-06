const webpack = require("webpack");

const ModuleFederationPlugin = require("webpack/lib/container/ModuleFederationPlugin");

module.exports = {
  output: {
    publicPath: "http://localhost:4200/",
    uniqueName: "__mfe_appName__",
  },
  optimization: {
    runtimeChunk: false,
  },
  plugins: [
    new ModuleFederationPlugin({
      name: "__mfe_appName__",
      library: { type: "var", name: "__mfe_appName__" },
      filename: "remoteEntry.js",
      exposes: {
        __mfe_appModuleName__: "./src/app/app.module.ts",
      },
      shared: {
        "@angular/core": { 
          singleton: true, 
          requiredVersion: 'auto', 
          eager: true,  // Enable this project on browser
        },
        "@angular/common": { 
          singleton: true, 
          requiredVersion: 'auto', 
          eager: true 
        },
        "@angular/router": { 
          singleton: true, 
          requiredVersion: 'auto', 
          eager: true 
        },
        "ngx-common-ui-lib": { 
          singleton: true, 
          requiredVersion: 'auto', 
          eager: true 
        },
        // "ngx-common-ui-lib": { singleton: true, requiredVersion: 'auto' }, // async loading (less bundle size if packages already presented in shell)
        // "ngx-common-ui-lib": { singleton: true, requiredVersion: '^0.0.13' }, // pass required lib version
        // "ngx-common-ui-lib": { eager: true, singleton: true }, // sync loading
      },
    }),
  ],
};
