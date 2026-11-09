/** Adds the id if absent, removes it if present. Returns a new array. */
export const toggleId = (ids: string[], id: string): string[] => (ids.includes(id) ? ids.filter(x => x !== id) : [...ids, id]);
