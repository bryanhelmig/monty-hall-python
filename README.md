## Monty Hall / Monty Python

The [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is quite fun to think about (and tease your friends over), and it is fun to code up as well. As soon as you start thinking through the logic, you are struck with the oddity of the problem!

Intuitively it doesn't quite make sense why you are better off switching, but as soon as you try to formalize it via sets you'll likely notice the operations you have to do remove several doors from the possible set (both your chosen door AND Monty's revealed door) yield a greater chance of winning.

The output of the script is below, but I'd encourage everyont to try modeling this with code like `set(range(door_count)) - {chosen_door, revealed_door}`! Otherwise, [check out the code](https://github.com/bryanhelmig/monty-hall-python/blob/master/main.py#L13-L21).

```
$ python3 main.py
66419 out of 100000 wins (66.419%) if you switch
33199 out of 100000 wins (33.199%) if you do not switch
```
