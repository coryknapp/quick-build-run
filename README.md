# quick-build-run
quickly build a c++ file based on comments in the file's header

quick-build-run scans the top comments of a c(++) file looking for any that
starts with "//qbr" then executes any commands it finds after.

For example:

```c++
//qbr echo this is executed
//this is not
//qbr echo this is executed
void some_function(){
//qbr echo this is not because a noncomment line preceded it.
}
```

As a more realistic example, one of my test c++ files starts with this

```c++
//[normal header stuff]
//[author, file description, whatever]
//qbr clang++ -std=c++11 test.cpp -lsfml-graphics -lsfml-window -lsfml-system
//qbr ./a.out
```
