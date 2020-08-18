## Weather Mini Challenge
Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

If the air humidity on a given day is **greater** than **70%**, it is a good idea to take an umbrella with you.
Your goal is to fetch the Ribeirão Preto air humidity forecast for the next **five** days from https://openweathermap.org/api and display the following message template:

*You should take an umbrella in these days: ....*

For instance, if on the next five days air humidity will be greater than 70% on Monday, Tuesday and Wednesday, you must display the message:

*You should take an umbrella in these days: Monday, Tuesday and Wednesday.*

**Fork this repo and send a link to the fork with your solution, please do not open pull requests.** 



# Solution by Ahlan Guarnier

### Featuring:
 - Docker version 19.03.12
 - Docker Compose version 1.26.2 
 
### Starting up
Build images:


```
$ docker-compose build
```


Start apps:

```
$ docker-compose up
```