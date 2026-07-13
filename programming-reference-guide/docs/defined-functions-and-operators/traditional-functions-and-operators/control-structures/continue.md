




# <span>Continue Statement</span> `:Continue`



A `:Continue` statement starts the next iteration of the immediately surrounding   `:For`, `:Repeat` or `:While` control loop.


When executed within a `:For` loop, the effect is to start the body of the loop with the next value of the iteration variable.


When executed within a `:Repeat` or `:While` loop, if there is a trailing test that test is executed and, if the result is true, the loop is terminated.  Otherwise the leading test is executed in the normal fashion.



