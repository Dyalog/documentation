# Arrays

A Dyalog APL data structure is called an array.  An array is a rectangular arrangement of items, each of which may be a single number, a single character, a namespace reference (ref), another array, or the `⎕OR` of an object.  An array which is part of another array is also known as a subarray.

An array has two properties; structure and data type.  Structure is identified by rank, shape, and depth.

## Rank

An array may have 0 or more axes or dimensions.  The number of axes of an array is known as its rank.  Dyalog APL supports arrays with a maximum of 15 axes.

- An array with 0 axes (rank 0) is called a scalar.
- An array with 1 axis (rank 1) is called a vector.
- An array with 2 axes (rank 2) is called a matrix.
- An array with more than 2 axes is called a multi-dimensional array.

## Shape

Each axis of an array may contain zero or more items.  The number of items along each axis of an array is called its shape.  The shape of an array is itself a vector.  Its first item is the length of the first axis, its second item the length of the second axis, and so on.  An array, whose length along one or more axes is zero, is called an empty array.

## Depth

An array whose items are all simple scalars (that is, single numbers, characters or refs) is called a simple array.  If one or more items of an array is not a simple scalar (that is, is another array, or a `⎕OR`), the array is called a nested array.  A nested array may contain items which are themselves nested arrays.  The degree of nesting of an array is called its depth.  A simple scalar has a depth of 0.  A simple vector, matrix, or multi-dimensional array has depth 1.  An array whose items are all depth 1 subarrays has depth 2; one whose items are all depth 2 subarrays has depth 3, and so forth.

## Type

An array, whose elements are all numeric, is called a numeric array; its TYPE is numeric.  A character array is one in which all items are characters.  An array whose items contain both numeric and character elements is of MIXED type.
