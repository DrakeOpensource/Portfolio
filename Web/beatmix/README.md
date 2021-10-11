# Beat Mix

## Project Overview

In this project, I implemented the logic for a beat-making music machine. It is an application that can loop over a 16-step grid of four drum types and play them when they are activated. There is also functionality to invert each row of drums, clear each row of drums, or clear the entire board. Finally, there is also a way to retrieve and save presets from a server.

You can view a video demonstration of the final app [here](https://s3.amazonaws.com/codecademy-content/programs/build-apis/solution-videos/BeatMix480.mov).

## Implementation Details

**public/js/script.js**:
- Four variables to represent the arrays of drum pads. These arrays are named after the drums they represent: `kicks`, `snares`, `hiHats`, `rideCymbals`. These arrays all have a length of `16` and are initially filled with `false`.

- a function called `toggleDrum` that takes two arguments: a string representing the array name (`'kicks'`, `'snares'`, `'hiHats'`, or `'rideCymbals'`), and an index number. This function flips the boolean value in the correct array at the specified index.

- A function named `clear` that takes an array name string and sets all values in the correct array to `false`.

- A function named `invert` that takes an array name string and flips the boolean value of all elements in the correct array.


**presetHandler.js**:

- a function named `presetHandler`. This function is called from within the server to get an existing preset or create/update a preset.

  - `presetHandler` takes up to three arguments. The first argument is a string representing the request type: `'GET'` or `'PUT'`. The second argument is the array index of the `presets` array. For `'PUT'` requests, a third argument, `newPresetArray` will also be passed in, representing the new drum preset array to save at that index.

  - `presetHandler` returns an array. This array will have one or two elements depending on how it is called. If `presetHandler` is called with an invalid `index`, it returns an array with `404` as the first element, meaning that that array index is <a href="https://en.wikipedia.org/wiki/HTTP_404" target="_blank">Not Found</a>. If `index` is valid, the first element of the return array is `200`, meaning the request was <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200" target="_blank">OK</a>.
  
  - If `presetHandler` is called a method that is not `'GET'` or `'PUT'`, it returns an array with `400` as the first element, meaning that it was a <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400" target="_blank">Bad Request</a>.
  
  - If the index was valid, `presetHandler` returns a second element in the array. for `'GET'` requests, that element is the preset array at that array index. For `'PUT'` requests, it saves the `newPresetArray` to that index and then also return it as the second element.


### Bonus

Additionally, there is a function in **script.js** to play multiple synthesizer tones at once via:

- a function called `getNeighborPads` that accepts an x, y, and a size parameter. In the application, these values refer to the synth grid: `x` and `y` zero-indexed from the bottom left of the grid, and `size` is a number representing the number of rows/columns in the square. `getNeighborPads` returns an array of neighbors, each in the form `[xValue, yValue]`. Neighbors are the squares immediately to the left, right, above, and below of a grid position.


## Testing

There is a testing suite to check for all essential functionality and
edge cases.