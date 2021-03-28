# Documentation Enhancement with open science practices at sktime

[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/sktime/community) [![Matrix](https://img.shields.io/badge/matrix-%23sktime%3Asktime.org-blue.svg)](https://www.sktime.org/en/latest/how_to_get_started.html) [![Discord](https://img.shields.io/discord/475789330380488707?color=blueviolet&label=discord)](https://discord.com/invite/gqSab2K)


## Welcome!

Thank you for visiting the *Documentation Enhancement with open science practices* project repository. Find out more about the project below.

## :seedling: What are we doing?

**Vision statement:**
To make it easier for users and developers of sktime to recognize their contributions more visibly and formally to encourage long-term maintenance of their contributions

### The problem
There is a lack of an estimator overview in sktime linking code (classes or functions), with their docstring, the contributor and literature. This makes it hard for users when they have a question to ask about any particular code or an algorithm.

### The solution
To solve the problem, we need to implement an automated learning algorithm. 

## :ear_of_rice: Who are we?

Project lead: [Afzal Ansari](https://github.com/afzal442) and Abdulelah Al Mesfer

Read more about

## Acknowledgments

This project is developed as part of the [Open Life Science](https://openlifesci.org/) program, with mentorship from [Toby Hodges](https://github.com/tobyhodges).

README was inspired by [STEMM Role Models App](https://github.com/KirstieJane/STEMMRoleModels/blob/gh-pages/README.md).


## Install

These instructions are basic; you can use any method to do this work. The important part is making sure that you follow the checklist below before publishing the repository.

```sh
# Let's make a new folder
mkdir new-repo && cd new-repo
# Start a Git instance and copy over template files.
git init
cp ../repo-template/* .
# Overwrite this README
mv README.md setup-checklist.md
mv example-README.md README.md
# Go over and check off the checklist, and finally
rm setup-checklist
```

## Checklist

Go through this checklist after creating your repository. It should only take a couple of minutes; if there is a way to make this more efficient, open an issue and let's talk about it here! \m/

### README
- [ ] Copy `example-README.md` from this repository to your directory.
- [ ] Rename all instances of `<Replace Title>` in README to match the new repo title
- [ ] Manually go through and edit the rest of the README.

### Other Files
- [ ] Copy `CODE_OF_CONDUCT.md` verbatim.
- [ ] Copy `CONTRIBUTING.md` and ensure that you've added any repository-specific instructions. (Replace `<Replace Title>` again).
- [ ] Should you have a `CHANGELOG.md`? Document your release process, if you plan on having one, in the `CONTRIBUTING.md` file.

### Dotfiles
- [ ] Do you need a `.gitignore` file?
- [ ] Do you need an `.npmignore` file?

### License
- [ ] Copy the MIT license from the example repo.
- [ ] Is `Haja Networks Oy` the licensor?
- [ ] Have you added `MIT` as the license in the `package.json`?
- [ ] If you made changes, were these reflected in the last section of the README?

### GitHub Metadata
- [ ] Have you added a short description to the repository?
  - [ ] Is the description matched in the byline under the title in the README?
- [ ] Have you added topics to the GitHub repository: `orbitdb`, `orbit`, and so on?
  - [ ] Have you added these topics as keywords in the `package.json`?

### `package.json`

- [ ] Is the `author` field correct?
- [ ] Have you added `keywords`?
- [ ] Are the `bugs` and `homepage` fields correct?
- [ ] Have you added tests? Are they matched, here?
- [ ] Have you added a `lint` command, if using [`eslint-config-orbitdb`](https://github.com/orbitdb/eslint-config-orbitdb)?

### Tests

- [ ] Are there automated tests?
- [ ] ...for the browser as well?
- [ ] Are those reflected in CI?
- [ ] Bonus points: Using CircleCI workflows to segment tests?
- [ ] Extra bonus points: Are you cross-testing dependencies (i.e. are changes in `orbit-db-keystore` tested in `orbit-db` as well

### Benchmarks
- [ ] Are there benchmarks?
- [ ] Did you run the benchmarks before / after the change or PR?

### Examples
- [ ] Is there an example folder with usage examples?
- [ ] For the browser as well?

## Contribute

If you think this could be better, please [open an issue](https://github.com/afzal442/DocumentationEnhancementAtsktime/issues/new)!

Please note that all interactions in [@afzal442](https://github.com/afzal442) fall under our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE) © 2021
