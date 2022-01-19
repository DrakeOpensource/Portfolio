// gets the preset array
const presets = require('./presets');

const presetHandler = (requestType, index, newPresetArray) => {
    // handles preset requets and returns appropriate HTTP/array
    if (requestType === 'GET'){
        // 'GET' request
        if (presets[index]){
            // if preset is valid return: [Valid Request, Presets]
            return [200, presets[index]];
        } else {
            // return: [Not Found]
            return [404];
        }
    } else if (requestType === 'PUT'){
        // 'PUT' request
        if (!presets[index]){
            // checks for validity of preset[index]
            // if invalid return: [Not Found]
            return [404];
        } else {
            // if valid set new presets to the array and return: [Valid Request, New Presets]
            presets[index] = newPresetArray;
            return [200, presets[index]];
        }
    } else {
        // invalid request type, return: [Bad Request]
        return [400];
    }
};


// Leave this line so that your presetHandler function can be used elsewhere:
module.exports = presetHandler;
