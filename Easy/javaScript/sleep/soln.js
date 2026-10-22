/**
 * @param {number} millis
 * @return {Promise}
 */
var sleep = async function (millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
};