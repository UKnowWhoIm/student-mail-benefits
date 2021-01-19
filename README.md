# Student Benefits

An Open API containing all information regarding student licenses for popular professional products.

## Table Of Contents
- [Using the API](#using-the-api)
  - [Routes](#routes)

### Using the API

### Routes

| Route | Method | Function |
| ----- | ----- | ----- |
| /benefits/ | GET |  [Get All Benefits](#get-all-benefits) |
| /benefits/ | POST | [Create a benefit](#create-a-benefit) |
| /benefits/&lt;PK&gt;/ | GET | [Fetch Benefit By PK](#fetch-benefit-by-pk) |
| /category/ | GET | [Get all categories](#get-all-categories) |
| /category/&lt;PK&gt; | GET | [Fetch Category by PK](#fetch-category-by-pk) |

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

Get all the verified benefits stored in this API.<br/>
To filter by category, pass category=&lt;category_id&gt; as a GET parameter

### Fetch Benefit By PK

Get details of Benefit by PK

### Create a Benefit

Contribute to this collection by adding an unlisted benefit

| Arguments | Type | Required |
| ----- | ----- | ----- | 
| title | String | Yes | 
| description | String | Yes |
| link | String | Yes |
| category | Integer | No |
| img_link | String | No |
| highlights | JSON String | No |

**NOTE**: Your contribution will be listed only after verification by community members.

### Get all Categories

Get all the categories.

### Fetch Category by PK

Fetch a category by it's PK

