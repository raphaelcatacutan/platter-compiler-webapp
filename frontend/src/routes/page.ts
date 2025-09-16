// frontend/src/routes/+page.ts
export async function load() {
  const res = await fetch('http://localhost:3000');
  const message = await res.text();
  return { message };
}
