A Python generator is 
1. a special kind of function (or expression) that produces values one at a time, 
2. lazily, instead of creating all values in memory at once.
3. function that returns an iterator and yields values one at a time using yield, preserving execution state between calls.

Generator vs Normal Function : 

| Feature      | Normal function    | Generator           |
| ------------ | ------------------ | ------------------- |
| Keyword      | `return`           | `yield`             |
| Execution    | Runs fully         | Pauses & resumes    |
| Memory       | Stores all results | One value at a time |
| Return value | Single value       | Iterator            |

Generator lifecycle : 
Created → Suspended → Running → Suspended → Exhausted
