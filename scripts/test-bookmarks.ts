import assert from 'node:assert/strict';
import { toggleId } from '../src/features/bookmarks/logic';
assert.deepEqual(toggleId([], 'a'), ['a']);
assert.deepEqual(toggleId(['a', 'b'], 'a'), ['b']);
const orig = ['x']; toggleId(orig, 'y'); assert.deepEqual(orig, ['x'], 'does not mutate input');
console.log('bookmark tests passed');
