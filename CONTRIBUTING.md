# Museum OpenAPI example contributing guide

Hi! We're really excited that you are interested in contributing to the Museum OpenAPI example.
Before submitting your contribution though, please make sure to take a moment and read through the following guidelines.

- [Museum OpenAPI example contributing guide](#museum-openapi-example-contributing-guide)
  - [Issue reporting guidelines](#issue-reporting-guidelines)
  - [Pull request guidelines](#pull-request-guidelines)
  - [Development setup](#development-setup)
  - [Contribute documentation](#contribute-documentation)
    - [Configuration file](#configuration-file)
  - [Project structure](#project-structure)
  - [Release flow](#release-flow)

## Issue reporting guidelines

- Before opening a new issue, check that the same problem or idea hasn't already been reported.
  You can do that on the [Issues page](https://github.com/Redocly/museum-openapi-example/issues) in the repository and using the filter `is:issue` combined with some keywords relevant to your idea or problem.
  It helps us notice that more people have the same issue or use-case, and reduces the chance of getting your issue marked as a duplicate.
  Plus, you can even find some workarounds for your issue in the comments of a previously reported one!

- The best way to get your bug fixed is to provide a (reduced) test case.
  A test case means listing and explaining the steps we should take to try and hit the same problem you're having.
  It helps us understand in which conditions the issue appears, and gives us a better idea of what may be causing it.

- Abide by our [Code of Conduct](https://redocly.com/code-of-conduct/) in all your interactions on this repository, and show patience and respect to other community members.

## Pull request guidelines

Before submitting a pull request, please make sure the following is done:

1. Fork the repository and create your branch from `main`.
2. Clone the repo to your local device, so you can run it and test visually before submitting your changes.
3. Create a branch from `main` before making any updates.
4. Make you updates to the `openapi.yaml` file.
5. Run `npm install` in the repository root to see your updates locally.
6. Once you are happy with your updates, commit and push your updates to your fork.
7. Open a PR from your repo/branch to the Redocly repo/main.

## Development setup

[Node.js](http://nodejs.org) at v14.19.0+ and NPM v7.0.0+ are required.

After cloning the repo, install the Redocly CLI by running the following command:

```bash
npm install # or npm i
```

To preview the Museum OpenAPI example's docs and your changes, run the following command:

```bash
npm run preview
```

## Contribute documentation

Additions and updates to our documentation are very welcome.


### Configuration file

The **redocly.yaml** file is the  
Please refer to the [configuration file](https://redocly.com/docs/cli/configuration/) documentation for more details.

## Project structure

- **`docs`**: contains the documentation source files. 
When changes to the documentation are merged, they automatically get published on the [Redocly docs website](https://redoc.ly/docs/cli/).


## Release flow

If the pipelines are not starting, close and reopen the PR. Merging that PR triggers the release process.
