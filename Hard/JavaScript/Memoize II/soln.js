/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    const RESULT = Symbol("result");

    return function (...args) {
        let node = cache;

        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());
            }

            node = node.get(arg);
        }

        if (node.has(RESULT)) {
            return node.get(RESULT);
        }

        const result = fn.apply(this, args);
        node.set(RESULT, result);

        return result;
    };
}