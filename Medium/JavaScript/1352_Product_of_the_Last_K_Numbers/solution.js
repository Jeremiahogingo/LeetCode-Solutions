

/**
 * @constructor
 */
var ProductOfNumbers = function() {
    // Sentinel value simplifies prefix product calculations.
    this.prefixProducts = [1];
};

/**
 * Appends a number to the stream.
 *
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    // Zero invalidates every prefix product that spans it.
    if (num === 0) {
        this.prefixProducts = [1];
        return;
    }

    const lastProduct =
        this.prefixProducts[this.prefixProducts.length - 1];

    // Store the cumulative product.
    this.prefixProducts.push(lastProduct * num);
};

/**
 * Returns the product of the last k numbers.
 *
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    const n = this.prefixProducts.length;

    // The requested range includes a zero.
    if (k >= n) {
        return 0;
    }

    // Divide the latest prefix product by the
    // prefix product immediately before the range.
    return (
        this.prefixProducts[n - 1] /
        this.prefixProducts[n - 1 - k]
    );
};


/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */