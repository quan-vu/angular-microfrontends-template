# Angular Microfrontends Template

A template for quickstart your Microfrontends project with Angular.

Easy to use with install script.

Feature

- Manage and Deploy Microfrontend app independence based on its own repository.
- Each Microfrontend app has its own CI pipeline.

## TODO

**MFE genererator CLI**

  - [x] Clone angular.json file from angular.mfe.json template file.
  - [ ] Clone webpack.config.js file from webpack.config.mfe.js template file.

## Guide

Step 1: Create fresh Angular Projects

```shell
# MFR shell
rm -rf ./shell
ng new shell
cd shell && yarn add --dev ngx-build-plus

# MFE layout
rm -rf ./layout
ng new layout
cd layout && yarn add --dev ngx-build-plus

# MFE dashboardPage
rm -rf ./dashboardPage
ng new dashboardPage
cd dashboardPage && yarn add --dev ngx-build-plus

# MFE samplePage
rm -rf ./samplePage
ng new samplePage
cd samplePage && yarn add --dev ngx-build-plus
```