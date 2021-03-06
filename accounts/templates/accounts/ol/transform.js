/**
 * @module ol/transform
 */
import {assert} from './asserts.js';


/**
 * An array representing an affine 2d transformation for use with
 * {@link module:ol/transform} functions. The array has 6 elements.
 * @typedef {!Array.<number>} Transform
 */


/**
 * Collection of affine 2d transformation functions. The functions work on an
 * array of 6 elements. The element order is compatible with the [SVGMatrix
 * interface](https://developer.mozilla.org/en-US/docs/Web/API/SVGMatrix) and is
 * a subset (elements a to f) of a 3×3 matrix:
 * ```
 * [ a c e ]
 * [ b d f ]
 * [ 0 0 1 ]
 * ```
 */


/**
 * @private
 * @type {module:ol/transform~Transform}
 */
var tmp_ = new Array(6);


/**
 * Create an identity transform.
 * @return {!module:ol/transform~Transform} Identity transform.
 */
export function create() {
  return [1, 0, 0, 1, 0, 0];
}


/**
 * Resets the given transform to an identity transform.
 * @param {!module:ol/transform~Transform} transform Transform.
 * @return {!module:ol/transform~Transform} Transform.
 */
export function reset(transform) {
  return set(transform, 1, 0, 0, 1, 0, 0);
}


/**
 * Multiply the underlying matrices of two transforms and return the result in
 * the first transform.
 * @param {!module:ol/transform~Transform} transform1 Transform parameters of matrix 1.
 * @param {!module:ol/transform~Transform} transform2 Transform parameters of matrix 2.
 * @return {!module:ol/transform~Transform} transform1 multiplied with transform2.
 */
export function multiply(transform1, transform2) {
  var a1 = transform1[0];
  var b1 = transform1[1];
  var c1 = transform1[2];
  var d1 = transform1[3];
  var e1 = transform1[4];
  var f1 = transform1[5];
  var a2 = transform2[0];
  var b2 = transform2[1];
  var c2 = transform2[2];
  var d2 = transform2[3];
  var e2 = transform2[4];
  var f2 = transform2[5];

  transform1[0] = a1 * a2 + c1 * b2;
  transform1[1] = b1 * a2 + d1 * b2;
  transform1[2] = a1 * c2 + c1 * d2;
  transform1[3] = b1 * c2 + d1 * d2;
  transform1[4] = a1 * e2 + c1 * f2 + e1;
  transform1[5] = b1 * e2 + d1 * f2 + f1;

  return transform1;
}

/**
 * Set the transform components a-f on a given transform.
 * @param {!module:ol/transform~Transform} transform Transform.
 * @param {number} a The a component of the transform.
 * @param {number} b The b component of the transform.
 * @param {number} c The c component of the transform.
 * @param {number} d The d component of the transform.
 * @param {number} e The e component of the transform.
 * @param {number} f The f component of the transform.
 * @return {!module:ol/transform~Transform} Matrix with transform applied.
 */
export function set(transform, a, b, c, d, e, f) {
  transform[0] = a;
  transform[1] = b;
  transform[2] = c;
  transform[3] = d;
  transform[4] = e;
  transform[5] = f;
  return transform;
}


/**
 * Set transform on one matrix from another matrix.
 * @param {!module:ol/transform~Transform} transform1 Matrix to set transform to.
 * @param {!module:ol/transform~Transform} transform2 Matrix to set transform from.
 * @return {!module:ol/transform~Transform} transform1 with transform from transform2 applied.
 */
export function setFromArray(transform1, transform2) {
  transform1[0] = transform2[0];
  transform1[1] = transform2[1];
  transform1[2] = transform2[2];
  transform1[3] = transform2[3];
  transform1[4] = transform2[4];
  transform1[5] = transform2[5];
  return transform1;
}


/**
 * Transforms the given coordinate with the given transform returning the
 * resulting, transformed coordinate. The coordinate will be modified in-place.
 *
 * @param {module:ol/transform~Transform} transform The transformation.
 * @param {module:ol/coordinate~Coordinate|module:ol/pixel~Pixel} coordinate The coordinate to transform.
 * @return {module:ol/coordinate~Coordinate|module:ol/pixel~Pixel} return coordinate so that operations can be
 *     chained together.
 */
export function apply(transform, coordinate) {
  var x = coordinate[0];
  var y = coordinate[1];
  coordinate[0] = transform[0] * x + transform[2] * y + transform[4];
  coordinate[1] = transform[1] * x + transform[3] * y + transform[5];
  return coordinate;
}


/**
 * Applies rotation to the given transform.
 * @param {!module:ol/transform~Transform} transform Transform.
 * @param {number} angle Angle in radians.
 * @return {!module:ol/transform~Transform} The rotated transform.
 */
export function rotate(transform, angle) {
  var cos = Math.cos(angle);
  var sin = Math.sin(angle);
  return multiply(transform, set(tmp_, cos, sin, -sin, cos, 0, 0));
}


/**
 * Applies scale to a given transform.
 * @param {!module:ol/transform~Transform} transform Transform.
 * @param {number} x Scale factor x.
 * @param {number} y Scale factor y.
 * @return {!module:ol/transform~Transform} The scaled transform.
 */
export function scale(transform, x, y) {
  return multiply(transform, set(tmp_, x, 0, 0, y, 0, 0));
}


/**
 * Applies translation to the given transform.
 * @param {!module:ol/transform~Transform} transform Transform.
 * @param {number} dx Translation x.
 * @param {number} dy Translation y.
 * @return {!module:ol/transform~Transform} The translated transform.
 */
export function translate(transform, dx, dy) {
  return multiply(transform, set(tmp_, 1, 0, 0, 1, dx, dy));
}


/**
 * Creates a composite transform given an initial translation, scale, rotation, and
 * final translation (in that order only, not commutative).
 * @param {!module:ol/transform~Transform} transform The transform (will be modified in place).
 * @param {number} dx1 Initial translation x.
 * @param {number} dy1 Initial translation y.
 * @param {number} sx Scale factor x.
 * @param {number} sy Scale factor y.
 * @param {number} angle Rotation (in counter-clockwise radians).
 * @param {number} dx2 Final translation x.
 * @param {number} dy2 Final translation y.
 * @return {!module:ol/transform~Transform} The composite transform.
 */
export function compose(transform, dx1, dy1, sx, sy, angle, dx2, dy2) {
  var sin = Math.sin(angle);
  var cos = Math.cos(angle);
  transform[0] = sx * cos;
  transform[1] = sy * sin;
  transform[2] = -sx * sin;
  transform[3] = sy * cos;
  transform[4] = dx2 * sx * cos - dy2 * sx * sin + dx1;
  transform[5] = dx2 * sy * sin + dy2 * sy * cos + dy1;
  return transform;
}


/**
 * Invert the given transform.
 * @param {!module:ol/transform~Transform} transform Transform.
 * @return {!module:ol/transform~Transform} Inverse of the transform.
 */
export function invert(transform) {
  var det = determinant(transform);
  assert(det !== 0, 32); // Transformation matrix cannot be inverted

  var a = transform[0];
  var b = transform[1];
  var c = transform[2];
  var d = transform[3];
  var e = transform[4];
  var f = transform[5];

  transform[0] = d / det;
  transform[1] = -b / det;
  transform[2] = -c / det;
  transform[3] = a / det;
  transform[4] = (c * f - d * e) / det;
  transform[5] = -(a * f - b * e) / det;

  return transform;
}


/**
 * Returns the determinant of the given matrix.
 * @param {!module:ol/transform~Transform} mat Matrix.
 * @return {number} Determinant.
 */
export function determinant(mat) {
  return mat[0] * mat[3] - mat[1] * mat[2];
}

//# sourceMappingURL=transform.js.map