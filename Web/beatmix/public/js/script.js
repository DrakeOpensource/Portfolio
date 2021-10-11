
// Drum Arrays
let kicks = new Array(16).fill(false);
let snares = new Array(16).fill(false);
let hiHats = new Array(16).fill(false);
let rideCymbals = new Array(16).fill(false);

const getDrumArray = (drumType) => {
    // gets the valid drum arrays from the string param
    switch (drumType) {
        case 'kicks':
            return kicks;
        case 'snares':
            return snares;
        case 'hiHats':
            return hiHats;
        case 'rideCymbals':
            return rideCymbals;
        default:
            return;
    }
};

const toggleDrum = (arrayName, index) => {
    const drumArray = getDrumArray(arrayName); 
    // getting drum array from arrayName
    if (index > 15 || index < 0 || !drumArray){
        // checking for valid index and array
        return;
    } else {
        drumArray[index] = !drumArray[index];
        // flipping the value at array index
    }
};

const clear = (arrayName) => {
    const drumArray = getDrumArray(arrayName); 
    // getting drum array from arrayName
    if (drumArray){
        drumArray.fill(false);   
        // checking for valid and array
    } else {
        return;
    }
};

const invert = (arrayName) => {
    const drumArray = getDrumArray(arrayName); 
    // getting drum array from arrayName
    if (drumArray){
        // check for valid array
        drumArray.forEach((value, index, array) => {
            array[index] = !value;})
        // flipping each boolean in the drum array
    } else {  
        return;  

    }
};

const getNeighborPads = (x, y, size) => {
    // x, y: synth grid location
    // size: num of rows/columns in the square
    let neighborArray = [];
    if (x >= size || x < 0 || y >= size || y < 0 || size < 1){
                // returns an empty array if invalid location
        return neighborArray;
    } else {
        neighborArray.push([x+1, y]);
        // right neighbor
        neighborArray.push([x-1, y]);
        // left neighbor
        neighborArray.push([x, y+1]);
        // up neighbor
        neighborArray.push([x, y-1]);
        // down neighbor

        return neighborArray.filter((neighborLoc) => {
            // using filter to select elements that pass test
            return neighborLoc.every((loc) => {
                // making sure every location is valid
                return loc >= 0 && loc < size;
                // returning if not negative and not greater than pad size
            });  
        });
    }
};
