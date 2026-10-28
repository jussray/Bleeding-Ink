import { cp, copyFile, mkdir, rm, stat } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Build only public assets. Never publish repository notes, receipts or drafts by accident.
const root = resolve(fileURLToPath(new URL('..', import.meta.url)));
const target = join(root, 'dist');
const required = ['index.html', 'assets/skeleton-machine-cutout.webp', 'assets/sign-detail.webp', 'img/sign.jpg', 'img/key-visual.jpg', 'img/baskets.jpg'];
const files = ['index.html', 'robots.txt', 'sitemap.xml'];
const dirs = ['assets', 'img'];

for (const rel of required) {
  try { const st = await stat(join(root, rel)); if (!st.isFile()) throw new Error('not a file'); }
  catch { throw new Error('Build blocked: missing required public asset '+rel); }
}
await rm(target, {recursive:true, force:true});
await mkdir(target, {recursive:true});
for (const name of files) {
  try { if ((await stat(join(root, name))).isFile()) await copyFile(join(root,name),join(target,name)); }
  catch (error) { if (error?.code !== 'ENOENT') throw error; }
}
for (const name of dirs) {
  try { if ((await stat(join(root, name))).isDirectory()) await cp(join(root,name), join(target,name), {recursive:true}); }
  catch (error) { if (error?.code !== 'ENOENT') throw error; }
}
console.log('Static preview staged to ./dist (no deployment performed).');
