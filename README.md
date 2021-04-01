# Student Benefits

An Open API containing all information regarding student licenses for popular professional products.

## Table Of Contents
- [Using the API](#using-the-api)
  - [Routes](#routes)
- [Becoming a maintainer](#becoming-a-maintainer)
- [Workflow](Workflow.md)


### Using the API

### Routes

| Route | Method | Function |
| ----- | ----- | ----- |
| /api/benefits/ | GET |  [Get All Benefits](#get-all-benefits) |
| /api/benefits/ | POST | [Suggest a new benefit](#suggest-a-new-benefit) |
| /api/benefits/&lt;PK&gt; | GET | [Fetch Benefit By PK](#fetch-benefit-by-pk) |
| /api/benefits/&lt;PK&gt;/ | PUT | [Suggest changes for benefit](#suggest-edits-to-a-benefit) |
| /api/category/ | GET | [Get all categories](#get-all-categories) |
| /api/category/&lt;PK&gt; | GET | [Fetch Category by PK](#fetch-category-by-pk) |

### Benefit Data

| Arguments | Type | Details |
| ----- | ----- | ----- | 
| id | Integer | Primary Key | 
| title | String | Title of the benefit | 
| description | String | A small description of the benefit |
| link | String | Link to the website of the benefit |
| category | Integer | The category of the benefit |
| img_link | String | The link to the image of the benefit |
| highlights | JSON String | JSON List of Strings containing important features of the benefit |


### Get All Benefits

Get all the verified benefits stored in this API.

To filter by category, pass category=&lt;category_id&gt; as a GET parameter

To search by title, pass search=&lt;title&gt; as a GET parameter

### Fetch Benefit By PK

Get details of Benefit by PK

### Benefit Format

| Arguments | Type | Required |
| ----- | ----- | ----- | 
| title | String | Yes | 
| description | String | Yes |
| link | String | Yes |
| category | Integer | No |
| img_link | String | No |
| highlights | JSON String | No |
| email | String | No |

**NOTE**: If email is provided, and the contribution is accepted, the user can potentially become a maintainer.


### Suggest a new benefit

Contribute to this collection by adding an unlisted benefit.

For a frontend form visit `/benefits/new`

Your contribution will be listed only after verification by community members.

All contributions without approval for a week are automatically deleted


### Suggest edits to a benefit

Found something wrong? Improve it by suggesting changes.

For a frontend form visit `/benefits/edit`

Your changes would only be made public after verification by community members.

All contributions without approval for a week are automatically deleted
### Get all Categories

Get all the categories.

### Fetch Category by PK

Fetch a category by it's PK

### Becoming a maintainer

If you regularly contribute to this API, you will have the chance to become a maintainer.

As a maintainer,
  - All your new changes will instantly be approved
  - You'll get a chance to review changes from the community
