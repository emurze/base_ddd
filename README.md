# Created base DDD

* Domain
* Application
* Infrastructure
* IoC container


### Domain

* Contains dataclasses, abc and etc - Business Objects
* Should also contain DAO (Object used to access data)
* Should not depend on *external* libs


### Infrastructure - DAL

* DAL that contains of DAO - DATA ACCESS OBJECTS ( Repository pattern )
* Can depend on the *external* libs 
* Can also depend on Application and Domain


### Application

* Should not depend on *external* libs
* Business logic
* Should use Domain and Infrastructure


### IoC container

* Provides launch of the Service


### Features

* Django Model is DAO ( Object to access data)
* DAL Layer is classes that contain difficult queries to simplify their names


### Clean ( Onion ) Architecture

![clean](public/clean.jpg)