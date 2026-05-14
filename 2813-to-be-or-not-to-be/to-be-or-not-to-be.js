var expect = function(val) {
    return {
        toBe: (v) => {
            if (val === v) return true;
            throw new Error("Not Equal");
        },
        notToBe: (v) => {
            if (val !== v) return true;
            throw new Error("Equal");
        }
    }
};