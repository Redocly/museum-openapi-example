# Redocly Museum API Example

An imaginary, but delightful Museum API for interacting with museum services and information. Built by Redocly for educational purposes. Enjoy!

> [!NOTE]  
> This OpenAPI description uses the [OpenAPI 3.1.0 specification](https://spec.openapis.org/oas/v3.1.0).

## Overview

Introducing the "Museum API", which offers a set of endpoints to interact with a museum's services--such as retrieving museum hours, managing special events, and purchasing tickets. 

New functionality may be added to the Museum API in the future. Is there an example you'd like to see? Please [open an issue](https://github.com/Redocly/museum-openapi-example/issues/new).

## Features
> [!NOTE]  
> Reminder that this is a fictional example for learning purposes. The features below are only for learning.

The Museum API has the following core features (sorted by tags):
- Operations
  - Get museum operational hours
- Special events
  - Get special event data
  - List special events
  - Create and update a special event
  - Delete a special event
- Tickets
  - Purchase museum tickets for general entry or special events
  - Get scannable QR code for museum ticket

## Getting started

1. Clone this repo.
2. Open the repo in your IDE.
3. Run `npm install` to install the Redocly CLI.

### Working with the OpenAPI description

We encourage you to explore the museum's OpenAPI description and make changes. Try experimenting with the following approaches:

**Preview the museum's API docs and observe your changes visually.**
- Run `npm run preview` to preview the documentation.
- Navigate to the **List special events** operation in the preview.
- With the preview running...
  - Go to the _openapi.yaml_ file in your IDE.
  - Search for `listSpecialEvents` to find the matching `operationId`.
  - Replace the `description` field with the snippet below:
```yaml
    description: |-
        Return a list of _upcoming_ special events at the museum.
            
        See one you like? Use this API to [buy a ticket](/#tag/Tickets/operation/buyMuseumTickets).  
```
See the updated description? This is a great way to preview how end-users of your docs will experience your changes.

**Lint your changes to the OpenAPI description using [Redocly CLI](https://redocly.com/docs/cli/).**
- Open the museum's _openapi.yaml_ file in your IDE. 
- Add the following snippet to `paths` above the /museum-hours operation:
```yaml
  /example:
    get: 
      summary: Example Summary
      description: Example description
      responses: 
        '200':
          description: Success
        '400': 
          description: Bad Request
```
- Run `npm run lint` in your terminal. See the errors? 

The linting behavior is controlled by the _redocly.yaml_ configuration file. The linter is configured to use Redocly's [recommended ruleset](https://redocly.com/docs/cli/rules/recommended/#recommended-ruleset), which are built into the CLI. However, we also added a [configurable rule](https://redocly.com/docs/cli/rules/configurable-rules/) for enforcing sentence casing on operation summaries. 
