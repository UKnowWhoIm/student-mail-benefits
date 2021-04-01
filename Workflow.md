## Workflow

This file contains an explanation of the workflow implemented.

### Creation of a new benefit

- A successful POST request to `/api/benefits/` won't create a Benefit object, but instead a Contribution object
- This Contribution object contains actual benefit as a JSON object(after validation) along with email and datetime
- If approved, the JSON object is used to create a new benefit, which will be linked to this Contribution object

### Editing a benefit

- A successful PUT request to `/api/benefits/<PK>/` creates a Contribution object
- The current benefit will be linked to it, and the changes for the benefit will be stored in the json field
- If approved, the JSON object is used to modify the benefit

### Maintainers

| TABLE | CREATE | READ | UPDATE | DELETE |
| --- | --- | --- | --- | --- |
| Contributions | YES | YES | YES | NO |
| Benefits | NO | YES | NO | NO |
| Category | YES | YES | NO | NO |

If a Contribution is made by maintainers, it will be approved automatically

#### Becoming a maintainer

- After the approval of a contribution made by a non maintainer, their total contributions will be checked against a 
  threshold using django post save signal in `benefits.signals.handlers`
- If it surpasses the threshold, the email will be placed in the MailLists table
- A regular routine sends the unsent emails in MailList every day
- On clicking the link received in the email, the user can enter a password and become a maintainer.


### Management Commands

#### `create_group`

Run once to create the maintainer group to set up permissions for maintainers.

#### `execute_routine`

- Run periodically to send pending invites, delete old invites and contributions.
- Arguments: `--no-email`, `-- no-invites`, `--no-contributions`