# Student Benefits

An Open API containing all information regarding student licenses for popular professional products.

## Table Of Contents
- [Using the API](#using-the-api)
  - [Routes](#routes)
- Contributing

### Using the API

#### Routes

| Route | Method | Function |
| ----- | ----- | ----- |
| /benefits/ | GET |  [Get All Benefits](#get-all-benefits) |
| /benefits/ | POST | [Create a benefit](#fetch-benefit-by-pk) |
| /benefits/&lt;PK&gt;/ | GET | [Fetch Benefit By PK](#create-a-benefit) |

##### Get All Benefits

Get all the verified benefits stored in this API

##### Fetch Benefit By PK

Get details of Benefit by PK

##### Create a Benefit

Contribute to this collection by adding an unlisted benefit

| Arguments | Type | Required |
| ----- | ----- | ----- | 
| title | String | Yes | 
| description | String | Yes |
| link | String | Yes |
| category | Integer | No |
| img_link | String | No |


