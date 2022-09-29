- [Installation](#installation)

### Installation

#### Clone repo

``` bash
# clone the repo
$ git clone https://github.com/Huxteen/supply-chain-app.git

# go into app's directory
$ cd supply-chain-app

# Build docker-compose
$ docker-compose build

## Run test and Flake8
$ docker-compose run app sh -c "python manage.py test && flake8"

# start project
$ docker-compose up


# App Endpoints 

# Account App
## create User ['POST]
    {{base_url}}api/accounts/create/

## Login user to get token ['POST']
    {{base_url}}api/accounts/token/

## Retrieve Login user details ['GET]
    {{base_url}}api/accounts/update/

## Update Login user details ['PUT', 'PATCH']
    {{base_url}}api/accounts/update/


# Product App
## List Product ['GET']
    {{base_url}}api/products/

## Create Product ['POST']
    {{base_url}}api/products/

## Product Detail View ['GET']
    {{base_url}}api/products/4/

## Update Product View ['PUT', 'PATCH']
    {{base_url}}api/products/4/


# Address App
## List Address ['GET']
    {{base_url}}api/address/

## Create Address ['POST']
    {{base_url}}api/address/

## Address Detail View ['GET']
    {{base_url}}api/address/4/

## Update Address View ['PUT', 'PATCH']
    {{base_url}}api/address/4/


# Order App
## List Order ['GET']
    {{base_url}}api/order/

## Create Order ['POST']
    {{base_url}}api/order/

## Order Detail View ['GET']
    {{base_url}}api/order/4/

## Update Order View ['PUT', 'PATCH']
    {{base_url}}api/order/4/



