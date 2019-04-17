/**
 * @module ol/TileQueue
 */
import TileState from './TileState.js';
import {listen, unlisten} from './events.js';
import EventType from './events/EventType.js';
import PriorityQueue from './structs/PriorityQueue.js';


/**
 * @typedef {function(module:ol/Tile, string, module:ol/coordinate~Coordinate, number): number} PriorityFunction
 */


var TileQueue = (function (PriorityQueue) {
  function TileQueue(tilePriorityFunction, tileChangeCallback) {

    PriorityQueue.call(
      /**
       * @param {Array} element Element.
       * @return {number} Priority.
       */
      this, function(element) {
        return tilePriorityFunction.apply(null, element);
      },
      /**
       * @param {Array} element Element.
       * @return {string} Key.
       */
      function(element) {
        return (/** @type {module:ol/Tile} */ (element[0]).getKey());
      });

    /**
     * @private
     * @type {function(): ?}
     */
    this.tileChangeCallback_ = tileChangeCallback;

    /**
     * @private
     * @type {number}
     */
    this.tilesLoading_ = 0;

    /**
     * @private
     * @type {!Object.<string,boolean>}
     */
    this.tilesLoadingKeys_ = {};

  }

  if ( PriorityQueue ) TileQueue.__proto__ = PriorityQueue;
  TileQueue.prototype = Object.create( PriorityQueue && PriorityQueue.prototype );
  TileQueue.prototype.constructor = TileQueue;

  /**
   * @inheritDoc
   */
  TileQueue.prototype.enqueue = function enqueue (element) {
    var added = PriorityQueue.prototype.enqueue.call(this, element);
    if (added) {
      var tile = element[0];
      listen(tile, EventType.CHANGE, this.handleTileChange, this);
    }
    return added;
  };

  /**
   * @return {number} Number of tiles loading.
   */
  TileQueue.prototype.getTilesLoading = function getTilesLoading () {
    return this.tilesLoading_;
  };

  /**
   * @param {module:ol/events/Event} event Event.
   * @protected
   */
  TileQueue.prototype.handleTileChange = function handleTileChange (event) {
    var tile = /** @type {module:ol/Tile} */ (event.target);
    var state = tile.getState();
    if (state === TileState.LOADED || state === TileState.ERROR ||
        state === TileState.EMPTY || state === TileState.ABORT) {
      unlisten(tile, EventType.CHANGE, this.handleTileChange, this);
      var tileKey = tile.getKey();
      if (tileKey in this.tilesLoadingKeys_) {
        delete this.tilesLoadingKeys_[tileKey];
        --this.tilesLoading_;
      }
      this.tileChangeCallback_();
    }
  };

  /**
   * @param {number} maxTotalLoading Maximum number tiles to load simultaneously.
   * @param {number} maxNewLoads Maximum number of new tiles to load.
   */
  TileQueue.prototype.loadMoreTiles = function loadMoreTiles (maxTotalLoading, maxNewLoads) {
    var this$1 = this;

    var newLoads = 0;
    var abortedTiles = false;
    var state, tile, tileKey;
    while (this.tilesLoading_ < maxTotalLoading && newLoads < maxNewLoads &&
           this.getCount() > 0) {
      tile = /** @type {module:ol/Tile} */ (this$1.dequeue()[0]);
      tileKey = tile.getKey();
      state = tile.getState();
      if (state === TileState.ABORT) {
        abortedTiles = true;
      } else if (state === TileState.IDLE && !(tileKey in this$1.tilesLoadingKeys_)) {
        this$1.tilesLoadingKeys_[tileKey] = true;
        ++this$1.tilesLoading_;
        ++newLoads;
        tile.load();
      }
    }
    if (newLoads === 0 && abortedTiles) {
      // Do not stop the render loop when all wanted tiles were aborted due to
      // a small, saturated tile cache.
      this.tileChangeCallback_();
    }
  };

  return TileQueue;
}(PriorityQueue));


export default TileQueue;

//# sourceMappingURL=TileQueue.js.map