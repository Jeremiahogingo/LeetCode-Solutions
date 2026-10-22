# 2618. Check if Object Instance of Class

![LeetCode](https://img.shields.io/badge/LeetCode-2618-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow?logo=javascript)
![Topic](https://img.shields.io/badge/Topic-Prototype%20Chain-blue)

## Problem Overview

Implement `checkIfInstanceOf(obj, classFunction)` to determine whether a value is an instance of a given class or any of its superclasses.

Unlike JavaScript's standard `instanceof` operator, the solution must also support primitive values such as numbers by accounting for their corresponding wrapper objects.

**LeetCode:** [Check if Object Instance of Class](https://leetcode.com/problems/check-if-object-instance-of-class/)

## Approach: Prototype Chain

JavaScript uses prototype-based inheritance. An object's prototype chain links it to the prototypes of its parent classes, allowing it to access inherited methods.

The solution validates the inputs, converts primitive values into their corresponding wrapper objects using `Object(obj)`, and uses `instanceof` to check the prototype chain. <Cite refs={["turn661857search1","turn661857search3"]}/>

### Algorithm

1. Return `false` if `obj` is `null` or `undefined`.
2. Return `false` if `classFunction` is not a function.
3. Convert `obj` into an object using `Object(obj)`. Existing objects remain unchanged, while primitives are boxed.
4. Use `instanceof` to check whether `classFunction.prototype` exists in the object's prototype chain.
5. Return the resulting boolean.

## JavaScript Implementation

```javascript
/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
    if (
        obj === null ||
        obj === undefined ||
        typeof classFunction !== "function"
    ) {
        return false;
    }

    return Object(obj) instanceof classFunction;
};
```

## Example Walkthrough

### Example 1: Standard Instance

```javascript
checkIfInstanceOf(new Date(), Date);
// true
```

The object created by `new Date()` inherits from `Date.prototype`, so the check returns `true`.

### Example 2: Inheritance

```javascript
class Animal {}
class Dog extends Animal {}

checkIfInstanceOf(new Dog(), Animal);
// true
```

A `Dog` instance inherits from `Animal.prototype` through its prototype chain. Therefore, it is also an instance of `Animal`.

### Example 3: Primitive Value

```javascript
checkIfInstanceOf(5, Number);
// true
```

Normally, `5 instanceof Number` returns `false` because `5` is a primitive. However, `Object(5)` creates a `Number` wrapper object, allowing the instance check to return `true`.

### Example 4: Invalid Value

```javascript
checkIfInstanceOf(null, Object);
// false
```

The function returns `false` immediately without attempting to inspect the prototype chain.

## Edge Cases

| Input | Expected Output | Explanation |
|---|---|---|
| `new Date(), Date` | `true` | Valid instance of `Date` |
| `new Dog(), Animal` | `true` | Inherited instance through a superclass |
| `Date, Date` | `false` | The `Date` constructor is not a `Date` instance |
| `5, Number` | `true` | Primitive is boxed into a `Number` object |
| `"hello", String` | `true` | Primitive is boxed into a `String` object |
| `true, Boolean` | `true` | Primitive is boxed into a `Boolean` object |
| `null, Object` | `false` | Null is rejected |
| `undefined, Object` | `false` | Undefined is rejected |
| `{}`, Date | `false` | Plain object does not inherit from `Date.prototype` |
| `{}, undefined` | `false` | Invalid class argument |

## Complexity Analysis

- **Time Complexity:** \(O(d)\), where \(d\) is the depth of the prototype chain examined by `instanceof`.
- **Auxiliary Space Complexity:** \(O(1)\) for the check itself. Boxing a primitive may create a temporary wrapper object.

## Key Takeaways

- JavaScript inheritance is implemented through prototype chains.
- The `instanceof` operator checks whether a constructor's prototype appears in an object's prototype chain.
- Primitive values require special handling because they are not objects themselves.
- `Object(value)` allows primitive values to be checked through their corresponding wrapper types.
- Input validation prevents invalid values from causing errors.

**Important:** This solution uses JavaScript's built-in `instanceof` operator, which is appropriate for this implementation. A version that manually traverses prototypes would be needed if the problem prohibited using `instanceof`.

## Related Problems

- [Array of Objects](https://leetcode.com/problemset/)
- [Function.prototype.call](https://leetcode.com/problemset/)
- [Promise Time Limit](https://leetcode.com/problems/promise-time-limit/)

---


## Reference

- [LeetCode Problem 2618](https://leetcode.com/problems/check-if-object-instance-of-class/)
- [MDN: `instanceof` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)

---

*Part of my [LeetCode Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions) repository.*