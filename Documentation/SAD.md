# Python Train Randomiser Webapplication Software Architecture Document
## Version

## Introduction
This webapplication allows for people to easily share their model railroad consists 
Ever since starting with modelrailroading I found my train consists or formations to be a bit repetitive, so I always changed them around with wacky and unrealistic combinations! DB coaches with a EMD F7? Sure fire!

# Background Info


## Use Cases
## UC1

## Project setup
In this chapter the 

### Packages and software
The project will be developed with Python 3.12 and will run with the Flask framework. The database used will 

### Version Control
The project will be versioned with Git and be found on GitHub.

### CI/CD
As of yet due to inexperience of the developer with setting up a CI/CD pipeline there is none.

### Deployment
The project will be deployed on a docker container on the developers homelab and will be reachable on the `trains.techgoyle.nl` subdomain. it will have an SSL cert.

## Database Design
Since this application uses lots of information pertaining to locomotives and rolling stock an extensive database will be needed that fields the following tables:
- Rolling stock
- Locomotives
- Type
- Traction
- Country
- Company
- Era
- Builder
- Manufacturer
- Article Number

Since the use of models of trains will be used it is important to use these in the data model for this application.

Additional information could be the date this formation was spotted and where.



## Class Design
This is of yet undecided as the developer is not yet familiar with 